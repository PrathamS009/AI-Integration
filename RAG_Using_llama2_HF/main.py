import os
from pdf_loading import extract_text_from_pdf, chunk_text
from embed_index import EmbeddingIndex
from rag import RAG

pdf_folder = r"D:\Github_Desktop\AI-Integration\RAG_Using_llama2_HF\pdf_data"
all_texts = []

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(pdf_folder, filename)
        print(f"📘 Loading {filename} ...")
        with open(file_path, "rb") as f:
            text = extract_text_from_pdf(f)
            all_texts.append(text)

if not all_texts:
    raise ValueError("❌ No PDF files found in pdf_data/")

full_text = "\n\n".join(all_texts)
chunks = chunk_text(full_text, chunk_size=800, overlap=100)

emb = EmbeddingIndex()
emb.build(chunks)

rag = RAG(emb)

print("\n✅ RAG system ready! Ask questions (type 'exit' to quit)\n")

while True:
    q = input("Ask Your Question: ")
    if q.lower() in ["exit", "quit", "q"]:
        break
    answer = rag.ask(q)
    print("\nAnswer:", answer, "\n")
