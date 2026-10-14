"""Capability-aware tool registry and deterministic fallback routing for IRIS.

This module does not claim to discover tools exposed by the ChatGPT host. The
host/adapter must register tools it can actually invoke. Unknown availability
is never treated as available; paid calls require an explicit budget approval.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Iterable, Any

class ToolState(str, Enum):
    AVAILABLE = "AVAILABLE"
    QUOTA_EXHAUSTED = "QUOTA_EXHAUSTED"
    UNAUTHORIZED = "UNAUTHORIZED"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"

@dataclass(frozen=True)
class ToolEntry:
    tool_id: str
    provider: str
    capabilities: frozenset[str]
    state: ToolState = ToolState.UNKNOWN
    free_tier: bool = True
    priority: int = 100
    daily_quota_remaining: int | None = None
    cost_per_call: float = 0.0
    requires_auth: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class RouteDecision:
    selected: ToolEntry | None
    candidates: tuple[str, ...]
    skipped: tuple[tuple[str, str], ...]
    reason: str

class ToolRegistry:
    """Registry with deterministic, policy-gated routing and failure cooldown."""
    def __init__(self) -> None:
        self._entries: dict[str, ToolEntry] = {}
        self._disabled: dict[str, str] = {}

    def register(self, entry: ToolEntry) -> None:
        if not entry.tool_id.strip() or not entry.provider.strip():
            raise ValueError("tool_id and provider must be non-empty")
        self._entries[entry.tool_id] = entry
        self._disabled.pop(entry.tool_id, None)

    def update_state(self, tool_id: str, state: ToolState, *, quota_remaining: int | None = None) -> None:
        if tool_id not in self._entries:
            raise KeyError(tool_id)
        old = self._entries[tool_id]
        self._entries[tool_id] = ToolEntry(
            tool_id=old.tool_id, provider=old.provider, capabilities=old.capabilities,
            state=state, free_tier=old.free_tier, priority=old.priority,
            daily_quota_remaining=quota_remaining if quota_remaining is not None else old.daily_quota_remaining,
            cost_per_call=old.cost_per_call, requires_auth=old.requires_auth, metadata=old.metadata,
        )
        if state in (ToolState.QUOTA_EXHAUSTED, ToolState.UNAVAILABLE, ToolState.UNAUTHORIZED):
            self._disabled[tool_id] = state.value
        else:
            self._disabled.pop(tool_id, None)

    def list_entries(self) -> list[ToolEntry]:
        return sorted(self._entries.values(), key=lambda e: (e.provider.casefold(), e.tool_id.casefold()))

    def choose(self, capability: str, *, paid_allowed: bool = False,
               budget_remaining: float = 0.0, exclude: Iterable[str] = ()) -> RouteDecision:
        excluded = set(exclude)
        candidates = sorted(
            (e for e in self._entries.values() if capability in e.capabilities),
            key=lambda e: (not e.free_tier, e.priority, e.provider.casefold(), e.tool_id.casefold()),
        )
        skipped: list[tuple[str, str]] = []
        eligible: list[ToolEntry] = []
        for e in candidates:
            if e.tool_id in excluded:
                skipped.append((e.tool_id, "ALREADY_ATTEMPTED")); continue
            if e.tool_id in self._disabled:
                skipped.append((e.tool_id, self._disabled[e.tool_id])); continue
            if e.state != ToolState.AVAILABLE:
                skipped.append((e.tool_id, e.state.value)); continue
            if e.daily_quota_remaining is not None and e.daily_quota_remaining <= 0:
                skipped.append((e.tool_id, "QUOTA_EXHAUSTED")); continue
            if not e.free_tier and not paid_allowed:
                skipped.append((e.tool_id, "PAID_NOT_APPROVED")); continue
            if not e.free_tier and e.cost_per_call > budget_remaining:
                skipped.append((e.tool_id, "BUDGET_EXCEEDED")); continue
            eligible.append(e)
        if not eligible:
            return RouteDecision(None, tuple(e.tool_id for e in candidates), tuple(skipped), "NO_ELIGIBLE_TOOL")
        selected = eligible[0]
        return RouteDecision(selected, tuple(e.tool_id for e in candidates), tuple(skipped), "FREE_FIRST" if selected.free_tier else "PAID_APPROVED_FALLBACK")

    def invoke_with_fallback(self, capability: str, invoke: Callable[[ToolEntry], Any], *,
                             paid_allowed: bool = False, budget_remaining: float = 0.0) -> dict[str, Any]:
        attempted: list[str] = []
        events: list[dict[str, str]] = []
        while True:
            decision = self.choose(capability, paid_allowed=paid_allowed,
                                   budget_remaining=budget_remaining, exclude=attempted)
            events.extend({"tool_id": tid, "reason": reason} for tid, reason in decision.skipped)
            if decision.selected is None:
                return {"status": "BLOCKED", "reason": decision.reason,
                        "attempted": attempted, "routing_events": events}
            entry = decision.selected
            attempted.append(entry.tool_id)
            try:
                result = invoke(entry)
                # Adapter should return an explicit failure envelope for HTTP/provider errors.
                if isinstance(result, dict) and result.get("status") in {"QUOTA_EXHAUSTED", "UNAVAILABLE", "UNAUTHORIZED", "RATE_LIMITED"}:
                    state = ToolState.QUOTA_EXHAUSTED if result["status"] in {"QUOTA_EXHAUSTED", "RATE_LIMITED"} else ToolState(result["status"])
                    self.update_state(entry.tool_id, state)
                    events.append({"tool_id": entry.tool_id, "reason": state.value})
                    continue
                return {"status": "OK", "tool_id": entry.tool_id, "provider": entry.provider,
                        "result": result, "attempted": attempted, "routing_events": events}
            except Exception as exc:
                # Never retry the same tool automatically; mark it unavailable for this registry session.
                self.update_state(entry.tool_id, ToolState.UNAVAILABLE)
                events.append({"tool_id": entry.tool_id, "reason": f"INVOKE_ERROR:{type(exc).__name__}"})
