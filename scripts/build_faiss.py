import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

DATA_PATH = "../data/raw/"
INDEX_PATH = "../data/faiss_index/"

def load_documents():
    docs = []
    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_PATH, file))
            docs.extend(loader.load())
    return docs

def build_index():
    print("Loading documents...")
    documents = load_documents()

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("Building FAISS index...")
    vector_store = FAISS.from_documents(documents, embeddings)

    os.makedirs(INDEX_PATH, exist_ok=True)
    vector_store.save_local(INDEX_PATH)

    print("FAISS index created successfully!")

if __name__ == "__main__":
    build_index()