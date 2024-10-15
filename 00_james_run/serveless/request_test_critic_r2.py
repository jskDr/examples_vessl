import requests
from datetime import datetime
import time
 
base_url = "https://serve-api.vessl.ai/api/v1/services/54655njwic77"
token = "YutpD5EmWhX7lZqaK5q5gzH7vUBa1Z5M"
 
r = requests.post(
    f"{base_url}/async",
    headers={"Authorization": f"Bearer {token}"},
    json={
        "data": {
            "inputs": "Hello. I'm Elon Musk. who are you?",
            "max_tokens": 512,
            "top_k": 10,
            "top_p": 0.95,
            "temperature": 0.0
           },
        "method": "POST",
        "path": "/generate"
    }
)
print("received")
print(f"[utctime : {datetime.utcnow()}] : {r.text}")
print(r)