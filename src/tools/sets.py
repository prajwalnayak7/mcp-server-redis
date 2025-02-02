from typing import List
from mcp.server.fastmcp import FastMCP
from redis.exceptions import RedisError
import json

from connection import redis_client
from server import mcp

@mcp.tool()
def set_add(key: str, *members: List[str]) -> str:
    """Add members to a Redis set
    
    Args:
        key: Redis set key
        members: Members to add
    """
    try:
        added = redis_client.sadd(key, *members)
        return f"Added {added} new members to set '{key}'"
    except RedisError as e:
        return f"Error: {str(e)}"

@mcp.tool()
def set_members(key: str) -> str:
    """Get all members of a Redis set
    
    Args:
        key: Redis set key
    """
    try:
        members = redis_client.smembers(key)
        return json.dumps(list(members), indent=2)
    except RedisError as e:
        return f"Error: {str(e)}"
