#add_data_to_vectordb

from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


loader = WebBaseLoader(
 web_paths=["https://www.educosys.com/course/genai"]
)
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # using this context is not lost in splitting and chunk size it takes care of left side and right side as well
all_splits = text_splitter.split_documents(docs)


print(all_splits)
# embeeded all the splits into vector db
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma(collection_name="educosys_genai_info", embedding_function=embeddings, persist_directory="./chroma_genai")
vectorstore.add_documents(documents=all_splits)
print(vectorstore._collection.count())  # Check total stored chunks

