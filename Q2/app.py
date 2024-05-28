"""
This is the main script for running the Flask application. It imports
functions from other scripts to handle document processing, question
answering, and serving API endpoints for user queries.
"""


from flask import Flask, request, jsonify
from process_document import load_and_process_document
from qa_pipeline import get_relevant_chunks, get_answer

# Load the document
file_path = "luke_skywalker_wikipedia_content.txt"

#Process the document, and create the vector store
library = load_and_process_document(file_path)

# Flask App Setup
app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Get the relevant chunks
    context = get_relevant_chunks(question, library)

    # Querying the Hugging Face Question-Answer(QA) model
    answer = get_answer(question, context)

    return jsonify({"question": question, "answer": answer})

if __name__ == '__main__':
    app.run(port=5000)
