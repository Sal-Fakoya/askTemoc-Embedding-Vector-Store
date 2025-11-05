# RAG File Structure

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

## 👥 Team Structure & Responsibilities

### Person A — Ingestion & Parsing (Ingest Team)
- **Web scrapers / document loaders**
- **OCR pipeline** 
- **Chunking strategies**
- **Document metadata management**
- **Raw-document store (SQLite)**

### Person B — Embeddings & Vector Store (Index Team)
- **Embedding pipeline**
- **Local vector DB** (Chroma/FAISS for MVP)
- **Vector index schema design**
- **Vector search API**

### Person C — Retrieval & LLM Orchestration (RAG/LLM Team)
- **Retrieval logic** (hybrid search for future)
- **Reranker integration**
- **Langchain chains** calling Ollama/remote models
- **Generation & prompt engineering**
- **Chat history management**

### Person D — Infra, Evaluation, QA & Dashboard (Ops/Eval Team)
- **CI/CD pipelines**
- **Docker & development environments**
- **OpenAPI/contract testing**
- **RAG evaluation** (DeepEval/RAGAS)
- **Admin dashboard endpoints/CRUD**
- **Deployment documentation**
  

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
