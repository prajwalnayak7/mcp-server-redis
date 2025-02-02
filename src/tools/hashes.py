from typing import Dict, Optional
from mcp.server.fastmcp import FastMCP
from redis.exceptions import RedisError
import json

from connection import redis_client
from server import mcp

@mcp.tool()
def hash_set(key: str, field_values: Dict[str, str]) -> str:
    """Set multiple hash fields
    
    Args:
        key: Redis hash key
        field_values: Dictionary of field-value pairs
    """
    try:
        redis_client.hset(key, mapping=field_values)
        return f"Successfully set {len(field_values)} fields in hash '{key}'"
    except RedisError as e:
        return f"Error: {str(e)}"

@mcp.tool()
def hash_get(key: str, field: Optional[str] = None) -> str:
    """Get hash fields
    
    Args:
        key: Redis hash key
        field: Optional specific field to get (if None, gets all fields)
    """
    try:
        if field:
            value = redis_client.hget(key, field)
            if value is None:
                return f"Field '{field}' not found in hash '{key}'"
            return str(value)
        else:
            values = redis_client.hgetall(key)
            return json.dumps(values, indent=2)
    except RedisError as e:
        return f"Error: {str(e)}"
