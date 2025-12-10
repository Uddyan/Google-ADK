from google.adk.agents.llm_agent import Agent


import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool


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



root_agent = Agent(
   model='gemini-2.5-flash',
   name='root_agent',
   description='A helpful assistant for user questions, with file creation capability.',
   instruction=(
       'You are a file management assistant. When asked to create a new file, '
       'you MUST use the "create_file" tool and provide the exact filename as an argument.'
   ),
   tools=[file_tool_instance,delete_file_tool_instance]
)
