from redis import Redis
from redis.exceptions import RedisError
from datetime import datetime
import json

from config import REDIS_CONFIG

# Global Redis client
redis_client = Redis(**REDIS_CONFIG)

def get_connection_status() -> dict:
    """Get Redis connection status"""
    try:
        redis_client.ping()
        return {
            "status": "connected",
            "timestamp": datetime.now().isoformat(),
            "config": {
                "host": REDIS_CONFIG["host"],
                "port": REDIS_CONFIG["port"],
                "db": REDIS_CONFIG["db"]
            }
        }
    except RedisError as e:
        return {
            "status": "disconnected",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }
