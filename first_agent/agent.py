
# personal mcp agent format from google adk
# ./adk_agent_samples/mcp_client_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

# IMPORTANT: Replace this with the ABSOLUTE path to your my_adk_mcp_server.py script
PATH_TO_YOUR_MCP_SERVER_SCRIPT = "E:\\DSA-Prowess\\Google-ADK\\first_agent_mcp_server.py" # <<< REPLACE

if PATH_TO_YOUR_MCP_SERVER_SCRIPT == "E:\\DSA-Prowess\\Google-ADK\\first_agent_mcp_server.py":
    print("WARNING: PATH_TO_YOUR_MCP_SERVER_SCRIPT is not set. Please update it in agent.py.")
    # Optionally, raise an error if the path is critical

# LLm agent and agent 
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='first_agent_mcp_server',
    instruction="Use the 'create_file' tool to create a new file with the specified name.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command='python3', # Command to run your MCP server script
                    args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT], # Argument is the path to the script
                )
            )
            # tool_filter=['load_web_page'] # Optional: ensure only specific tools are loaded
        )
    ],
)




# below is github tool code
# import os
# from google.adk.agents.llm_agent import Agent
# from google.adk.tools.mcp_tool import McpToolset
# from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
# from mcp import StdioServerParameters
# from dotenv import load_dotenv
# load_dotenv()
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# root_agent = Agent(
#   model='gemini-2.5-flash',
#   name="github_agent",
#   instruction="Help users interact with GitHub repos",
#   tools=[
#       McpToolset(
#           connection_params=StdioConnectionParams(
#                server_params = StdioServerParameters(
#                    command='npx',
#                    args=[
#                        "-y",
#                        "@modelcontextprotocol/server-github",
#                    ],
#                    env={
#                        "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
#                    }
#                ),
#            ),
#       )
#   ],
# )

# import os
# from google.adk.agents.llm_agent import Agent
# from google.adk.tools.mcp_tool import McpToolset
# from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
# from mcp import StdioServerParameters


# TARGET_FOLDER_PATH = "E:\\DSA-Prowess\\Google-ADK\\"


# root_agent = Agent(
#   model='gemini-2.5-flash',
#   name="filesystem_assistant_agent",
#   instruction="Help the user manage their files. You can list files, read files, etc.",
#   tools=[
#       McpToolset(
#           connection_params=StdioConnectionParams(
#                server_params = StdioServerParameters(
#                    command='npx',
#                    args=[
#                        "-y",
#                        "@modelcontextprotocol/server-filesystem",
#                        os.path.abspath(TARGET_FOLDER_PATH),
#                    ],
#                ),
#            ),
#       )
#   ],
# )



# Below code is to foramt LLM response in JSON format
# import os
# from google.adk.agents.llm_agent import Agent
# from pydantic import BaseModel
# from typing import List


# class DayPlan(BaseModel):
#    day: int
#    title: str
#    activities: List[str]
#    notes: str = ""




# class TravelItinerary(BaseModel):
#    destination: str
#    total_days: int
#    best_time_to_visit: str
#    itinerary: List[DayPlan]


# root_agent = Agent(
#    model="gemini-2.5-flash",
#    name="travel_itinerary_agent",
#    description="Creates structured travel itineraries for any destination",
#    output_schema=TravelItinerary,
#    tools=[],
# )







# import os
# from google.adk.agents.llm_agent import Agent
# from pydantic import BaseModel


# class MailOutput(BaseModel): # Derive your class from BaseModel , wherein subject and body is of type string 
#    subject: str
#    body: str


# root_agent = Agent(
#   model='gemini-2.5-flash',
#   name='mail_agent',
#   description='A helpful assistant for writing mails',
#   output_schema=MailOutput, # The response you got from LLM is completely in JSON formt 
#   tools=[]
# )



# from google.adk.agents.llm_agent import Agent


# import os
# from google.adk.agents.llm_agent import Agent
# from google.adk.tools import FunctionTool
# from google.adk.tools import google_search


# def create_file(filename: str) -> str:
#    """
#    Creates a new, empty file with the specified name in the current directory.
  
#    Args:
#        filename: The name of the file to create (e.g., 'educosys.txt').
      
#    Returns:
#        A success or error message confirming the file status.
#    """
#    try:
#        if os.path.exists(filename):
#            return f"Error: File '{filename}' already exists. No action taken."
#        else:
#            with open(filename, "w") as f:
#                pass
#            return f"Successfully created empty file: '{os.path.abspath(filename)}'."
  
#    except Exception as e:
#        return f"Error creating file '{filename}': {e}"


# file_tool_instance = FunctionTool(func=create_file)

# def delete_file(filename: str) -> str:
#    """
#    Deletes a file from the current directory.


#    Args:
#        filename: The name of the file to delete.


#    Returns:
#        A message confirming success or describing the error.
#    """
#    try:
#        if not os.path.isfile(filename):
#            return f"Error: File '{filename}' does not exist."
      
#        os.remove(filename)
#        return f"Successfully deleted file: '{os.path.abspath(filename)}'."
  
#    except Exception as e:
#        return f"Error deleting file '{filename}': {e}"


# delete_file_tool_instance = FunctionTool(func=delete_file)

# def list_all_files() -> str:
#    """
#    Lists all files and folders in the current directory.


#    Returns:
#        A formatted string containing all entries or an error message.
#    """
#    try:
#        items = os.listdir(".")
      
#        if not items:
#            return "The current directory is empty."


#        result = "Contents of current directory:\n"
#        for name in items:
#            path = os.path.abspath(name)
#            if os.path.isdir(name):
#                result += f"[DIR]  {path}\n"
#            else:
#                result += f"[FILE] {path}\n"
      
#        return result.strip()
  
#    except Exception as e:
#        return f"Error listing directory contents: {e}"


# list_files_tool_instance = FunctionTool(func=list_all_files)



# root_agent = Agent(
#    model='gemini-2.5-flash',
#    name='root_agent',
#    description='A helpful assistant for user questions, with file creation capability.',
#    instruction=(
#        'You are a file management assistant. When asked to create a new file, '
#        'you MUST use the "create_file" tool and provide the exact filename as an argument.'
#    ),
#    tools=[file_tool_instance,delete_file_tool_instance, list_files_tool_instance]
# )

## below you can use any other LLM model from the google.adk.models.lite_llm
# import os
# from google.adk.agents.llm_agent import Agent
# from google.adk.models.lite_llm import LiteLlm
# root_agent = Agent(
#    model=LiteLlm(model="anthropic/claude-3-haiku-20240307"),
#    name="claude_agent",
#    description="You are a helpful assistant to answer user queries",
#    tools=[],
# )
