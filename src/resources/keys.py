from mcp.server.fastmcp import FastMCP
import json
from connection import redis_client
from server import mcp

@mcp.resource("redis://keys/{pattern}")
def list_keys(pattern: str) -> str:
    """List Redis keys matching a pattern"""
    try:
        keys = redis_client.keys(pattern)
        return json.dumps({"keys": keys}, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})
