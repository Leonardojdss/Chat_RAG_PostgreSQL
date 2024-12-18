from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()

def connection_openai_Embeddings():
    embeddings = AzureOpenAIEmbeddings(
    model="text-embedding-3-large")
    return embeddings