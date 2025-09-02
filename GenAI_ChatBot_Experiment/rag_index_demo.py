from dotenv import load_dotenv
import os

from llama_index.core import VectorStoreIndex as vsi, SimpleDirectoryReader as sdr

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

#Writing if-else to check loading of API Key
if api_key:
    print("API key loaded successfully")
else:
    print("Failed to load API key")

PATH = r"YOUR PATH\pdf"

if not os.path.exists(PATH):
    print("NO PATH")
    
documents=sdr(PATH).load_data()


index=vsi.from_documents(documents)

engine=index.as_query_engine()

result=engine.query("ASK YOUR QUESTION HERE")

print(result)

index.storage_context.persist("File_Index")