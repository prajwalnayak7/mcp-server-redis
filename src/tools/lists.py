from typing import List
from mcp.server.fastmcp import FastMCP
from redis.exceptions import RedisError
import json

from connection import redis_client
from server import mcp

@mcp.tool()
def list_push(key: str, *values: List[str], side: str = "right") -> str:
    """Push values to a Redis list
    
    Args:
        key: Redis list key
        values: Values to push
        side: Which side to push to ("left" or "right")
    """
    try:
        if side.lower() == "left":
            result = redis_client.lpush(key, *values)
        else:
            result = redis_client.rpush(key, *values)
        return f"Successfully pushed {len(values)} values to '{key}'. New length: {result}"
    except RedisError as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_range(key: str, start: int = 0, end: int = -1) -> str:
    """Get a range of values from a Redis list
    
    Args:
        key: Redis list key
        start: Start index (default: 0)
        end: End index (default: -1 for all)
    """
    try:
        values = redis_client.lrange(key, start, end)
        return json.dumps(values, indent=2)
    except RedisError as e:
        return f"Error: {str(e)}"
