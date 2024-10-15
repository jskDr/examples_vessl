import requests

base_url = "https://serve-api.vessl.ai/api/v1/services/lfw5rojnj20t"
token = "Zyx0iIHwPpW48rSmOhVmvFNMrgjBr7zR"


response = requests.post(
    f"{base_url}/request/generate",
    headers={"Authorization": f"Bearer {token}"},
    json={
        "inputs": "What is Deep Learning?",
        "parameters": {"max_new_tokens": 1000}
    }
)
print(f"response: {response}")
# print(f"response json: {response.json()}")