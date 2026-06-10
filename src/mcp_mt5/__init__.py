"""MetaTrader 5 MCP Server"""

__version__ = "0.1.4"
__all__ = ["main", "mcp"]


def __getattr__(name):
    if name == "mcp":
        from .main import mcp
        return mcp
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def main():
    """Entry point for the MCP server CLI"""
    import os

    from dotenv import load_dotenv

    from .main import mcp

    # Load environment variables from .env file if it exists
    load_dotenv()

    # Determine transport mode from environment or default to stdio
    transport = os.getenv("MT5_MCP_TRANSPORT", "stdio")

    if transport in ("http", "sse"):
        host = os.getenv("MT5_MCP_HOST", "127.0.0.1")
        port = int(os.getenv("MT5_MCP_PORT", "8000"))
        mcp.run(transport=transport, host=host, port=port)
    else:
        # Default to stdio for MCP clients like Claude Desktop
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

