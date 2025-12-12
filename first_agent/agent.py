# agent.py


from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


def retrieve_info(query: str) -> str:
   """Search for info related to educosys genai course"""
   try:
       embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
       vector_store = Chroma(
           collection_name="educosys_genai_info",
           embedding_function=embeddings,
           persist_directory="./chroma_genai",
       )
       # in langchain easy to retrieve vector store 
       retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3}) # finding 3 similarity in chroma db


       print(f"Querying retrieve_context with: {query}")
       print("--------------------------------------------------------------")
       results = retriever.invoke(query)
       print(f"Retrieved documents: {len(results)} matches found")
       for i, doc in enumerate(results):
           print(f"Document {i + 1}: {doc.page_content[:100]}...")


       print("--------------------------------------------------------------")


       content = "\n".join([doc.page_content for doc in results])
       if not content:
           print(f"No content retrieved for query: {query}")
           return f"No reviews found for '{query}'."


       print("--------------------------------------------------------------")
       print(f"Returning content: {content[:200]}...")
       return content
   except Exception as e:
       print(f"Error in retrieve_context: {e}")
       return f"Error retrieving reviews for '{query}'. Please try again."


file_tool_instance = FunctionTool(func=retrieve_info)


root_agent = Agent(
  model='gemini-2.5-flash',
  name='root_agent',
  description='A helpful assistant for user questions, with rag capability',
  instruction=(
      'You are an educosys assistant that answers queries for educosys genai course '
      'you MUST use the "retrieve_info" tool and provide the exact info about educosys genai course'
  ),
  tools=[file_tool_instance]
)
