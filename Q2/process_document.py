"""
This script handles the loading and processing of the document,
including splitting it into chunks and creating a FAISS vector store.
"""

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_and_process_document(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0,
        length_function=len
    )
    docs = text_splitter.split_documents(documents)

    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedding = HuggingFaceEmbeddings(model_name=embedding_model_name)

    library = FAISS.from_documents(docs, embedding)
    return library

if __name__ == "__main__":
    file_path = "luke_skywalker_wikipedia_content.txt"
    library = load_and_process_document(file_path)
    print("Document processed and FAISS vector store created")
