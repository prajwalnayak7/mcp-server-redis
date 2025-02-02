from mcp.server.fastmcp import FastMCP
from redis.exceptions import RedisError

from connection import redis_client
from server import mcp

@mcp.tool()
def publish_message(channel: str, message: str) -> str:
    """Publish a message to a Redis channel
    
    Args:
        channel: Channel name
        message: Message to publish
    """
    try:
        receivers = redis_client.publish(channel, message)
        return f"Message published to {receivers} subscribers"
    except RedisError as e:
        return f"Error: {str(e)}"
