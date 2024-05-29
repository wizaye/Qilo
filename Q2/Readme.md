# Retrieval Augumented Generation (RAG) using web scraping data and Large Language Models (LLM)

## Overview
This project aims to design a Retrieval-Augmented Generation based on web scraping the content.
The project includes web scraping data present in `Luke Skywalker's` wikipedia page from `Star wars`.

Below is a flowchart depicting the overall process of the project:

![Flowchart](/images/Flowchart.png)

## Folder Structure and File Descriptions
### Main Directory

- **app.py**: The main application file that initializes and runs the project.
- **full_setup_gemini.py**: Script to set up the environment and dependencies specific to the Gemini model.
- **full_setup_hugging_face.py**: Script to set up the environment and dependencies specific to the Hugging Face model.
- **process_document.py**: A script to process and analyze documents.
- **qa_pipeline.py**: Contains the pipeline for the Question-Answering system.
- **scrape_wiki.py**: Script for scraping content from Wikipedia.
- **requirements.txt**: A file listing all the Python dependencies required to run the project.
- **luke_skywalker_wikipedia_content.txt**: A text file containing the Wikipedia content for Luke Skywalker.

### Hidden and Virtual Environment Directories

- **.gitignore**: Specifies files and directories to be ignored by git.
- **__pycache__/**: Directory for the Python bytecode cache.
- **.venv/**: Directory for the virtual environment used for the project.

## Getting Started

### Prerequisites

Ensure you have Python installed.

Setup a venv and activate it.

You can install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

### Starting the App Server
To run the app server using a Local LLM:
-  Run the `app.py` using the command 
```python 
flask --app app run 
```

To run the app server in a single full setup mode:
-  Run the `full_setup_hugging_face.py` using the command 
```python 
flask --app full_setup_hugging_face run 
```
To run the app server using a LLM(Gemini):
-  Run the `full_setup_gemini.py` using the command 
```python 
flask --app full_setup_gemini_face run 
```
### Serving Requests 
To make a post request:
- Make a post request to `http://localhost:5000/ask` with the json body format as:
```json
{
    "question":"Your Desired Question",
}

```