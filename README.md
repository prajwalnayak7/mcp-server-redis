[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/prajwalnayak7-mcp-server-redis-badge.png)](https://mseep.ai/app/prajwalnayak7-mcp-server-redis)

## Usage

The structure is as follows:
```
mcp-server-redis/
├── src/
│   ├── __init__.py
│   ├── main.py           # Main entry point
│   ├── config.py         # Configuration
│   ├── connection.py     # Redis connection management
│   ├── resources/        # Resource implementations
│   │   ├── __init__.py
│   │   ├── status.py     # Connection status resources
│   │   └── keys.py       # Key-related resources
│   └── tools/           # Tool implementations
│       ├── __init__.py
│       ├── basic.py     # Basic Redis operations
│       ├── lists.py     # List operations
│       ├── hashes.py    # Hash operations
│       ├── sets.py      # Set operations
│       └── pubsub.py    # Pub/Sub operations
├── tests/              # Test directory
│   └── __init__.py
├── README.md
└── pyproject.toml
```

To use this server, you'll need to:

Install the required dependencies:

[If not already installed] https://docs.astral.sh/uv/

`uv venv`

`source .venv/bin/activate`

`uv sync`

Refer to the .env.example file to configure your Redis connection by adding the appropriate variables.

Run the server:

`python src/server.py`

## Capabilities of this server

**Resources:**

- redis://status - Current connection status
- redis://info - Redis server information
- redis://keys/{pattern} - List keys matching a pattern

**Tools:**

- Basic operations:
    - get_value - Get a value
    - set_value - Set a value with optional expiry
    - delete_key - Delete a key
    - increment - Increment a numeric value
- List operations:
    - list_push - Push values to a list
    - list_range - Get range of list values
- Hash operations:
    - hash_set - Set hash fields
    - hash_get - Get hash fields
- Set operations:
    - set_add - Add to a set
    - set_members - Get set members
- Pub/Sub:
    - publish_message - Publish a message



Each tool includes error handling and returns meaningful responses. The server will automatically reconnect to Redis if the connection is lost.

You can test it with the MCP Inspector:
`mcp dev src/server.py`

Or install it in Claude Desktop:
`mcp install src/server.py`

## Example
```
User: What's the current Redis connection status?
LLM: Let me check the Redis connection status for you.

[Reading resource redis://status]

The Redis server is currently connected and running on localhost:6379, database 0.

User: Can you store my name "Alice" in Redis?
LLM: I'll help you store your name in Redis using the set_value tool.

[Calling set_value with key="name" value="Alice"]
Successfully set key 'name'

I've stored your name "Alice" in Redis under the key "name". Would you like me to verify the value was stored correctly by retrieving it?

User: Yes please verify it
LLM: I'll retrieve the value using the get_value tool.

[Calling get_value with key="name"]
Alice

Yes, I can confirm that your name "Alice" was successfully stored in Redis and can be retrieved correctly. The value matches exactly what we stored.
```

## 
This implementation provides a solid foundation for Redis integration through MCP. You can extend it further by adding more Redis commands as needed for your specific use case.
