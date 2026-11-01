"""Starts the local BI Pixie server for Claude Code.

.mcp.json runs this file with the Python environment that `uv run --locked` builds from
the plugin's uv.lock, so every package it imports is the exact version, source and hash
listed there. The server is the MIT licensed bipixie-mcp package, and this file only
calls its entry point, the same one as the `bipixie-mcp` command.
"""

from bipixie_mcp.server import main

if __name__ == "__main__":
    main()
