
"""
This script sets up the question-answering pipeline using Hugging Face's
pre-trained model and provides functions for retrieving relevant chunks
and generating answers to questions.
"""

from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def get_relevant_chunks(question, library):
    relevant_docs = library.similarity_search(question, k=3)
    return " ".join([doc.page_content for doc in relevant_docs])

def get_answer(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
