from mcp.server.fastmcp import FastMCP

# create mcp
mcp = FastMCP("AVA")

# Define prompts
@mcp.prompt()
def ava(user_name: str, user_title: str) -> str:
    """Global instructions for Artificial Virutal Assistant (AVA)"""
    with open("prompts/ava.md", "r") as file:
        template = file.read()
    return template.format(user_name=user_name, user_title=user_title)

# Add Resoruce
# Define resources
# FORMAT :
#@mcp.resouce - decorator
#@mcp.resouce(<Unique Resource Identifier (URI)>)
@mcp.resource("email-examples://3-way-intro")
def write_3way_intro() -> str:
    """Example of a 3-way intro email"""
    with open("email-examples/3-way-intro.md", "r") as file:
        return file.read()

@mcp.resource("email-examples://call-follow-up")
def write_call_followup() -> str:
    """Example of a call follow-up email"""
    with open("email-examples/call-follow-up.md", "r") as file:
        return file.read()

@mcp.resource("directory://all")
def get_directory() -> str:
    """Get the entire directory of contacts"""
    with open("directory.csv", "r") as file:
        return file.read()
