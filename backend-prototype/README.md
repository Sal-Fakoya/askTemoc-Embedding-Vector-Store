
# According to the Notion we agreed to, I am Person C

Folder I worked under: ```embeddings_service```. 

My file Structure:
```
embeddings_service/
├── app.py
├── requirements.txt
├── db/
│   └── chroma/
├── models/
│   └── __init__.py
└── utils/
    └── __init__.py
```

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

















