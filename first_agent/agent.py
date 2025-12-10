from google.adk.agents.llm_agent import Agent


import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool
from google.adk.tools import google_search


def create_file(filename: str) -> str:
   """
   Creates a new, empty file with the specified name in the current directory.
  
   Args:
       filename: The name of the file to create (e.g., 'educosys.txt').
      
   Returns:
       A success or error message confirming the file status.
   """
   try:
       if os.path.exists(filename):
           return f"Error: File '{filename}' already exists. No action taken."
       else:
           with open(filename, "w") as f:
               pass
           return f"Successfully created empty file: '{os.path.abspath(filename)}'."
  
   except Exception as e:
       return f"Error creating file '{filename}': {e}"


file_tool_instance = FunctionTool(func=create_file)

def delete_file(filename: str) -> str:
   """
   Deletes a file from the current directory.


   Args:
       filename: The name of the file to delete.


   Returns:
       A message confirming success or describing the error.
   """
   try:
       if not os.path.isfile(filename):
           return f"Error: File '{filename}' does not exist."
      
       os.remove(filename)
       return f"Successfully deleted file: '{os.path.abspath(filename)}'."
  
   except Exception as e:
       return f"Error deleting file '{filename}': {e}"


delete_file_tool_instance = FunctionTool(func=delete_file)

def list_all_files() -> str:
   """
   Lists all files and folders in the current directory.


   Returns:
       A formatted string containing all entries or an error message.
   """
   try:
       items = os.listdir(".")
      
       if not items:
           return "The current directory is empty."


       result = "Contents of current directory:\n"
       for name in items:
           path = os.path.abspath(name)
           if os.path.isdir(name):
               result += f"[DIR]  {path}\n"
           else:
               result += f"[FILE] {path}\n"
      
       return result.strip()
  
   except Exception as e:
       return f"Error listing directory contents: {e}"


list_files_tool_instance = FunctionTool(func=list_all_files)



root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions, with file creation capability.',
   instruction=(
       'You are a file management assistant. When asked to create a new file, '
       'you MUST use the "create_file" tool and provide the exact filename as an argument.'
   ),
   tools=[file_tool_instance,delete_file_tool_instance, list_files_tool_instance]
)

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
