import requests

base_url = "https://serve-api.vessl.ai/api/v1/services/9i2hayeqnl6d/request"
response = requests.get(base_url)

if response.status_code == 200:
    try:
        response_json = response.json()
        print(f"response json: {response_json}")
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
else:
    print(f"Request failed with status code {response.status_code}")
