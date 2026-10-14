import pytest
from runtime.tool_registry import ToolEntry, ToolRegistry, ToolState

def entry(name, *, free=True, state=ToolState.AVAILABLE, quota=5, priority=100, cost=0):
    return ToolEntry(name, name.split(':')[0], frozenset({'search'}), state, free, priority, quota, cost)

def test_free_first_even_when_paid_has_higher_priority():
    r=ToolRegistry(); r.register(entry('paid:one', free=False, priority=0, cost=1)); r.register(entry('free:one', free=True, priority=50))
    assert r.choose('search', paid_allowed=True, budget_remaining=5).selected.tool_id == 'free:one'

def test_quota_exhausted_skips_to_next_free_provider():
    r=ToolRegistry(); r.register(entry('free:a', quota=0)); r.register(entry('free:b', priority=2))
    assert r.choose('search').selected.tool_id == 'free:b'

def test_paid_requires_explicit_approval_and_budget():
    r=ToolRegistry(); r.register(entry('paid:a', free=False, cost=2))
    assert r.choose('search').selected is None
    assert r.choose('search', paid_allowed=True, budget_remaining=1).selected is None
    assert r.choose('search', paid_allowed=True, budget_remaining=2).selected.tool_id == 'paid:a'

def test_unknown_never_counts_as_available():
    r=ToolRegistry(); r.register(entry('unknown:a', state=ToolState.UNKNOWN))
    assert r.choose('search').selected is None

def test_runtime_quota_error_falls_back_without_repeating_same_tool():
    r=ToolRegistry(); r.register(entry('provider:a', priority=1)); r.register(entry('provider:b', priority=2))
    calls=[]
    def invoke(tool):
        calls.append(tool.tool_id)
        if tool.tool_id.endswith(':a'): return {'status':'RATE_LIMITED'}
        return {'answer':'ok'}
    out=r.invoke_with_fallback('search', invoke)
    assert out['status']=='OK' and out['tool_id']=='provider:b'
    assert calls == ['provider:a','provider:b']

def test_all_blocked_returns_blocked_without_paid_fallback():
    r=ToolRegistry(); r.register(entry('free:a', quota=0)); r.register(entry('paid:b', free=False, cost=1))
    out=r.invoke_with_fallback('search', lambda t: {'answer':'should not happen'})
    assert out['status']=='BLOCKED' and out['attempted']==[]
