# askTemoc (Person B)

## File Structure

```
asktemoc/
├── ingest_stub/
│   └── app.py
├── embed_stub/
│   └── app.py
├── query_stub/
│   └── app.py
├── docker-compose.yml
├── requirements.txt
└── README.md  
```

High-level split (4 people)

Person A — Ingestion & Parsing (Ingest Team)

Web scrapers / document loaders, OCR pipeline, chunking, document metadata, raw-document store (SQLite).

Person B — Embeddings & Vector Store (Index Team)

Embedding pipeline, local vector DB (Chroma/FAISS for MVP), vector index schema, vector search API.

Person C — Retrieval & LLM Orchestration (RAG/LLM Team)

Retrieval logic (hybrid later), reranker integration, Langchain chains that call Ollama (or remote model), generation & prompt engineering, chat history manager.

Person D — Infra, Evaluation, QA & Dashboard (Ops/Eval Team)

CI, Docker/dev environments, OpenAPI/contract tests, RAG evaluation pipeline (DeepEval/RAGAS), admin dashboard endpoints/CRUD, deployment docs.

## 🎯 Goal (Person B)

Build a microservice that:

### 🔄 Input Processing
- Takes in text chunks via an API endpoint

### 🤖 Embedding Generation  
- Converts text to embedding vectors using models like:
  - `all-MiniLM-L6-v2` (lightweight, fast)
  - `bge-m3` (multilingual, high performance)

### 💾 Vector Storage
- Stores embeddings in local vector databases:
  - **Chroma** (recommended for simplicity)
  - **FAISS** (Facebook's high-performance library)

### 🔍 Search Capabilities
- Supports similarity search queries
- Returns most relevant text chunks based on query vectors
