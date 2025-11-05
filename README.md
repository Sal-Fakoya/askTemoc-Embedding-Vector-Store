# askTemoc-Embedding-Vector-Store

High-level split (4 people)

Person A — Ingestion & Parsing (Ingest Team)

Web scrapers / document loaders, OCR pipeline, chunking, document metadata, raw-document store (SQLite).

Person B — Embeddings & Vector Store (Index Team)

Embedding pipeline, local vector DB (Chroma/FAISS for MVP), vector index schema, vector search API.

Person C — Retrieval & LLM Orchestration (RAG/LLM Team)

Retrieval logic (hybrid later), reranker integration, Langchain chains that call Ollama (or remote model), generation & prompt engineering, chat history manager.

Person D — Infra, Evaluation, QA & Dashboard (Ops/Eval Team)

CI, Docker/dev environments, OpenAPI/contract tests, RAG evaluation pipeline (DeepEval/RAGAS), admin dashboard endpoints/CRUD, deployment docs.
