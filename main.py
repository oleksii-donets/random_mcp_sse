from fastmcp import FastMCP
from random import random

mcp = FastMCP("Demo 🚀")

@mcp.tool
def random_float() -> float:
    """Return a random float in [0,1)."""
    return random()

if __name__ == "__main__":
    mcp.run()
