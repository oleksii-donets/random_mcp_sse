from fastmcp import FastMCP
from random import random
import os

mcp = FastMCP("Demo 🚀")

@mcp.tool
def random_float() -> float:
    """Return a random float in [0,1)."""
    return random()

@mcp.prompt
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Please summarize the following text:\n\n{text}"

# Static resource
@mcp.resource("config://version")
def get_version(): 
    return "2.0.1"

# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: int):
    # Fetch profile for user_id...
    return {"name": f"User {user_id}", "status": "active"}


if __name__ == "__main__":
    transport = os.getenv("TRANSPORT", "STDIO").upper()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    if transport == "STDIO":
        mcp.run(transport="stdio")
    elif transport == "HTTP":
        mcp.run(transport="http", host=host, port=port, path="/mcp")
    elif transport == "SSE":
        mcp.run(transport="sse", host=host, port=port, path="/sse")
    else:
        raise ValueError(f"Invalid TRANSPORT value: {transport}. Must be STDIO, HTTP, or SSE")
