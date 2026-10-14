"""MCP entry point that keeps the reported runtime version aligned with the package."""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mcp_server

# The legacy module constant was left at 0.6.16 in the 0.6.18 package.
# Override the module global before the server starts so all tool responses
# report the package version used by this launcher.
mcp_server.APP_VERSION = "0.6.19"

if __name__ == "__main__":
    asyncio.run(mcp_server.main())
