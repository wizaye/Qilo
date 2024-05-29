from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/vijayendhergatla/.config/gcloud/application_default_credentials.json"

# # Step 1: Scrape the Wikipedia page
# url = "https://en.wikipedia.org/wiki/Luke_Skywalker"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Step 2: Extract the content
# content = ""
# for paragraph in soup.find_all('p'):
#     content += paragraph.text

# # Step 3: Save the content to a .txt file
# file_path = "luke_skywalker_wikipedia_content.txt"
# with open(file_path, "w", encoding="utf-8") as file:
#     file.write(content)

# print(f"Content saved to {file_path}")

# Load the document
loader = TextLoader('luke_skywalker_wikipedia_content.txt')
documents = loader.load()

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    length_function=len
)
docs = text_splitter.split_documents(documents)


# Use Hugging Face embeddings
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Create a FAISS vector store from the documents
library = FAISS.from_documents(docs, embedding)

# Create a retriever
retriever = VectorStoreRetriever(vectorstore=library)

# Set up Flask
app = Flask(__name__)

def get_relevant_chunks(question):
    # Retrieve top 3 relevant chunks
    relevant_docs = library.similarity_search(question, k=3)
    return " ".join([doc.page_content for doc in relevant_docs])

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Get relevant chunks
    context = get_relevant_chunks(question)
    input_text = f"{context} {question}"
    # Query the Google Generative AI API
    genai.configure(api_key = 'AIzaSyC0azZmebSBcytmPGwdb5S7hquLliVGFDw')
    answer = genai.GenerativeModel('gemini-1.5-flash').generate_content(
        'Here are the contexts for the question:'+context+'and Here is the question:'+question+'only generate the answer for the question if the question is relevant to the context and also donot disclose the context in the answer or whether it is relevant or not to the context',
    ).text
    return jsonify({"question": question, "answer": answer})

if __name__ == '__main__':
    app.run(port=5000)
