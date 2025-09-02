import os
from llama_index.core import (VectorStoreIndex as vsi, 
                              SimpleDirectoryReader as sdr, 
                              StorageContext as sc,
                              load_index_from_storage)
from dotenv import load_dotenv
from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
    question: str

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key loaded successfully")
else:
    print("Failed to load API key")

storage_context=sc.from_defaults(persist_dir="File_Index")

index=load_index_from_storage(storage_context)

engine=index.as_query_engine()

app=FastAPI()

@app.post("/")
async def root(item: Item):
    result=engine.query(item.question)
    return {"Answer:", result}

if __name__=="__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)