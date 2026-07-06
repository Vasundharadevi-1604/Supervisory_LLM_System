def build_prompt(query, docs):
    context = "\n".join([doc.page_content for doc in docs])

    return f"""
Answer ONLY based on the context below.
If unsure, say "I don't know".

Context:
{context}

Question:
{query}
"""