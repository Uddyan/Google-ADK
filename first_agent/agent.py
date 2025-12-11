# agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
import sys

# IMPORTANT: Replace this with the ABSOLUTE path to your my_adk_mcp_server.py script
PATH_TO_YOUR_MCP_SERVER_SCRIPT = "E:\\DSA-Prowess\\Google-ADK\\uddy_mcp_server.py" # <<< REPLACE

print(f"Using Python: {sys.executable}")
print(f"MCP Server: {PATH_TO_YOUR_MCP_SERVER_SCRIPT}")

root_agent = LlmAgent(
   model='gemini-2.0-flash',
   name='web_reader_mcp_client_agent',
   instruction="Use the 'create_file' tool to create a new file with the specified name.",
   tools=[
       McpToolset(
           connection_params=StdioConnectionParams(
               server_params = StdioServerParameters(
                   command=sys.executable, # Command to run your MCP server script
                   args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT], # Argument is the path to the script
               )
           )
           # tool_filter=['load_web_page'] # Optional: ensure only specific tools are loaded
       )
   ],
)
