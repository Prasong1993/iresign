"""Launcher for the consolidated IRIS MCP runtime."""
import asyncio, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from merged_mcp_server import main
if __name__ == '__main__': asyncio.run(main())
