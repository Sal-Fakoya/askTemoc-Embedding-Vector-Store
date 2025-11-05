import requests

resp = requests.post(
    "http://127.0.0.1:8002/search",
    json={"query": "Who is Temoc?", "top_k": 2}
)
print(resp.json())
