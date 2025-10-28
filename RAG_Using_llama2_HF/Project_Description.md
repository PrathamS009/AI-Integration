WorkFlow: Upload multiple PDFs, index them and interact with them


Libraries Required:
1. PyPDF: For uploading documents
2. transformers: to create a pipline to use llama2 model from hugging face
3. einops:
4. accelerate: to speed the process of uploading and loading of pipeline
5. langchain:
6. bitsandbytes:
7. sentence_transformers:
8. llama_index:

Step 1: Load your pdfs
    1. SimpleDirectoryReader - To read your pdfs from the path specified and load them
    2. VectorStoreIndex - To create vector index of the text from documents
    3. ServiceContext - The prompt that will pass with context and question to model
