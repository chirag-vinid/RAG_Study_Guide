# Copilot Instructions for Study_Guide (RAG_Study_Guide)

## Project Overview
This is a Python-based Retrieval-Augmented Generation (RAG) study guide system. It processes PDF study materials, extracts text, generates embeddings, and enables semantic search using vector stores (ChromaDB). The main workflow is orchestrated through several scripts, with a simple web interface for user interaction.

## Architecture & Key Components
- `app.py`: Likely the entry point for the web application (Flask or similar). Handles user requests and serves the UI (`index.html`).
- `main_rag.py`: Main logic for RAG workflow. Integrates PDF extraction, text chunking, embedding, and retrieval.
- `pdf_extracter.py`: Extracts text from uploaded PDFs. Output is stored in `extracted_text/`.
- `text_chunks.py`: Splits extracted text into manageable chunks for embedding and retrieval.
- `embedding.py`: Generates vector embeddings for text chunks, stores them in ChromaDB (`chroma_store_gemini/`).
- `index.html`: Frontend interface for user interaction.
- `requirements.txt`: Lists Python dependencies. Install with `pip install -r requirements.txt`.

## Data Flow
1. **Upload PDF** → `pdf_extracter.py` → `extracted_text/`
2. **Chunk Text** → `text_chunks.py` → processed chunks
3. **Embed Chunks** → `embedding.py` → ChromaDB (`chroma_store_gemini/`)
4. **Query/Answer** → `main_rag.py` (retrieves relevant chunks, generates answers)

## Developer Workflows
- **Setup**: Install dependencies with `pip install -r requirements.txt`.
- **Run App**: Likely `python app.py` (verify in `app.py`).
- **Debugging**: Use print/log statements; check `__pycache__/` for compiled files.
- **Data Storage**:
  - Extracted text: `extracted_text/`
  - Vector stores: `chroma_store_gemini/`, `vector_stores/`
  - Outputs: `outputs/`
  - Uploads: `uploads/`

## Conventions & Patterns
- Modular scripts for each pipeline stage (extract, chunk, embed, retrieve).
- Persistent storage for intermediate and final results (text, vectors).
- Use of ChromaDB for vector search; embeddings likely via Gemini or similar model.
- No test suite detected; manual testing via script execution and output inspection.
- No custom agent rules or conventions found in `.github/`, `README.md`, or agent files.

## Integration Points
- ChromaDB (local vector DB): `chroma_store_gemini/`
- PDF input/output: `uploads/`, `extracted_text/`
- Web frontend: `index.html` served by `app.py`

## Example Workflow
```bash
pip install -r requirements.txt
python app.py
# Upload PDF via web UI
# Text is extracted, chunked, embedded, and stored
# Query via UI to retrieve answers
```

## Key Files & Directories
- `app.py`, `main_rag.py`, `pdf_extracter.py`, `text_chunks.py`, `embedding.py`
- `index.html`, `requirements.txt`
- `chroma_store_gemini/`, `extracted_text/`, `uploads/`, `outputs/`, `vector_stores/`

---

**If any workflow or integration is unclear, please provide feedback so this guide can be improved.**
