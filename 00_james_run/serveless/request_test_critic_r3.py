import requests

url = 'https://serve-api.vessl.ai/api/v1/services/54655njwic77/request'
token = 'YutpD5EmWhX7lZqaK5q5gzH7vUBa1Z5M'
data = { "inputs": "Hello. I'm Elon Musk. who are you?",
            "max_tokens": 512,
            "top_k": 10,
            "top_p": 0.95,
            "temperature": 0.0
}

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)
print(response.text)