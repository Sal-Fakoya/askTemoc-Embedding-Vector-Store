### Person B — Embeddings & Vector Store (Index Team)
- **Embedding pipeline**
- **Local vector DB** (Chroma/FAISS for MVP)
- **Vector index schema design**
- **Vector search API**


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
  

🧠 Step 1: Install dependencies

Open a terminal inside the ```embeddings_service/``` folder and run:
```
pip install -r requirements.txt
```


🚀 Step 4: Run your server

Still inside the same folder, run:
```
uvicorn app:app --reload --port 8002
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8002 (Press CTRL+C to quit)
```

🎉 That means your FastAPI embedding service is now live!

