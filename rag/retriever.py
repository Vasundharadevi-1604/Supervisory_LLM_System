from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# -----------------------------
# FAISS Index Path
# -----------------------------
INDEX_PATH = "data/faiss_index/"


# -----------------------------
# Load Vector Retriever
# -----------------------------
def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db


# -----------------------------
# Evidence Retrieval Function
# -----------------------------
def retrieve_evidence(query, k=5):
    try:
        db = get_retriever()

        # Similarity Search
        docs = db.similarity_search(query, k=k)

        if not docs:
            print("No evidence retrieved.")
            return None

        # -----------------------------
        # DEBUG (VERY IMPORTANT)
        # -----------------------------
        print("\n===== RETRIEVED EVIDENCE =====")
        for i, doc in enumerate(docs, 1):
            print(f"{i}. {doc.page_content}")
        print("==============================\n")

        # Combine retrieved evidence
        evidence = "\n".join(
            [doc.page_content for doc in docs]
        )

        return evidence

    except Exception as e:
        print("Retriever Error:", e)
        return None