import requests

resp = requests.post(
    "http://127.0.0.1:8002/embed_batch",
    json={
        "items": [
            {"chunk_id": "1", "text": "UTD is a university in Texas.", "metadata": {"source": "test"}},
            {"chunk_id": "2", "text": "Temoc is UTD's mascot.", "metadata": {"source": "test"}}
        ]
    }
)
print(resp.json())
