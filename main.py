from fastmcp import FastMCP
from random import random

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
    mcp.run()
