from typing import Optional
from mcp.server.fastmcp import FastMCP
from redis.exceptions import RedisError

from connection import redis_client
from server import mcp

@mcp.tool()
def get_value(key: str) -> str:
    """Get value for a Redis key
    
    Args:
        key: Redis key to retrieve
    """
    try:
        value = redis_client.get(key)
        if value is None:
            return f"Key '{key}' not found"
        return str(value)
    except RedisError as e:
        return f"Error: {str(e)}"

@mcp.tool()
def set_value(key: str, value: str, expiry_seconds: Optional[int] = None) -> str:
    """Set value for a Redis key
    
    Args:
        key: Redis key to set
        value: Value to store
        expiry_seconds: Optional expiration time in seconds
    """
    try:
        redis_client.set(key, value, ex=expiry_seconds)
        return f"Successfully set key '{key}'"
    except RedisError as e:
        return f"Error: {str(e)}"

@mcp.tool()
def delete_key(key: str) -> str:
    """Delete a Redis key
    
    Args:
        key: Redis key to delete
    """
    try:
        result = redis_client.delete(key)
        if result == 1:
            return f"Successfully deleted key '{key}'"
        return f"Key '{key}' not found"
    except RedisError as e:
        return f"Error: {str(e)}"
