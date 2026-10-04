# ISO Quality Assistant

A local RAG (Retrieval-Augmented Generation) assistant for asking questions about the ISO 9001:2015 standard and the quality documents of a fictional manufacturing company, Atlas Composants. It searches the available documents, then uses a local Ollama model to write concise answers grounded in what it found, with the sources cited.
## Features

- Searches ISO and company documents stored in `data/`
- Uses LanceDB for local vector search
- Runs entirely locally with Ollama
- Provides a Streamlit chat interface
- Restricts responses to retrieved document content
- Lists only the files actually used in each answer

## Architecture

```text
User question
    ↓
Vector search with LanceDB
    ↓
Relevant document passages
    ↓
Agno agent + Ollama
    ↓
Answer with sources
```

## Project Structure

```text
IA-Agent-ISO/
├── data/                       # ISO and company documents to index
├── lancedb/                    # Generated local vector database
├── src/
│   └── iso_assistant/
│       ├── __init__.py
│       ├── config.py            # Paths, model names, and constants
│       ├── instructions.py      # Agent grounding rules
│       ├── knowledge.py         # LanceDB setup and document indexing
│       ├── agent.py             # Agent construction
│       └── ui.py                # Streamlit chat interface
├── app.py                       # Application entry point
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- [Ollama](https://ollama.com/)

## Installation

1. Clone the repository and open the project directory.

```powershell
git clone https://github.com/chaimakammoun/IA-Agent-ISO.git
cd IA-Agent-ISO
```


2. Install the Python dependencies.

```powershell
pip install streamlit agno lancedb
```

3. Download the Ollama models used by the application.

```powershell
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

## Add Documents

Place ISO standards, procedures, policies, or other source documents in the `data/` folder. The application indexes this directory when the agent is created.

## Run the Application

Make sure Ollama is running, then start Streamlit from the project root:

```powershell
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open it in your browser to use the assistant.

## Configuration

Model names, database settings, and project paths are defined in `src/iso_assistant/config.py`.

The default models are:

- Chat model: `llama3.2:3b`
- Embedding model: `nomic-embed-text`

## Data and Git

The `lancedb/` folder is generated locally and excluded from Git. Keep source documents in `data/` under version control only when they are appropriate to share.
