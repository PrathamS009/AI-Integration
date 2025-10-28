import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL")

class RAG:
    def __init__(self, emb_index):
        if not HF_TOKEN:
            raise ValueError("HF_TOKEN missing in .env")
        self.client = InferenceClient(provider="novita", api_key=HF_TOKEN)
        self.emb = emb_index

    def _make_prompt(self, question: str, context_chunks: list) -> str:
        context = "\n\n".join(context_chunks)
        return (f"""
            Use ONLY the information below to answer the question accurately.
            - Context:{context}
            - Question:{question}
            - Instructions
                - If the question is not properly asked or cannot be answered using the context, say 'The context does not provide that information'.
                - Do NOT repeat or mention the context.
                - Give a clear, concise answer based solely on the context.
                - If unsure, say 'The context does not provide that information.
        """
        )

    def ask(self, question: str, top_k: int = 4) -> str:
        chunks = self.emb.query(question, top_k=top_k)
        if not chunks:
            return "No relevant context found."

        prompt = self._make_prompt(question, chunks)

        result = self.client.chat.completions.create(
            model=HF_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a precise AI research assistant. "
                        "You MUST NOT reveal or repeat the context text. "
                        "Only output the answer clearly."
                    )
                },
                {"role": "user", "content": prompt}
            ],
        )
        try:
            return result.choices[0].message["content"].strip()
        except Exception:
            return str(result)
