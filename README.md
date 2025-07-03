# MCP Ollama Server

## MCP Server

`server.py` will hold the MCP server and the tools which we will expose to the agent/client.

## Client

the client will start the server in the background and retrieve available tools. the Client will run a connection directly with Ollama serving the SLM (Small Language Model)

### Ollama Chat Client

in order to query our user input we are required:

```python
import ollama
response = ollama.chat(
    model="deepseek-r1",
    messages=[
        {"role": "user", "content": "Explain Newton's second law of motion"},
    ],
)
print(response["message"]["content"])
```

#### Documentation

[Official Documentation for Getting Started with FastMCP](https://gofastmcp.com/getting-started/welcome)
[UV Basics](https://www.datacamp.com/tutorial/python-uv)
[Client Development](https://modelcontextprotocol.io/quickstart/client)
[Ollama MCP Stdio Client](https://medium.com/@jonigl/build-an-mcp-client-in-minutes-local-ai-agents-just-got-real-a10e186a560f)
[Anthropic MCP SSE Client](https://www.f22labs.com/blogs/mcp-practical-guide-with-sse-transport/)
[Adaptive Engineer MCP Server](https://newsletter.adaptiveengineer.com/p/build-a-custom-mcp-client-and-server)

**Videos**

[FastMCP Overview](https://www.youtube.com/watch?v=5xqFjh56AwM)