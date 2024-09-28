import requests

base_url = "https://serve-api.vessl.ai/api/v1/services/9i2hayeqnl6d"
token = "oBtcuRDdDQguWTydTBiG2RWhXCoSHHJF"


# Make the POST request
response = requests.post(
    f"{base_url}/request/generate",
    headers={"Authorization": f"Bearer {token}"},
    json={
        "inputs": "What is Deep Learning?",
        "parameters": {"max_new_tokens": 1000}
    }
)

# Print the response status code
print(f"response: {response}")

# Check if the request was successful
if response.status_code == 200:
    try:
        # Try to parse the JSON response
        response_json = response.json()
        print(f"response json: {response_json}")
    except requests.exceptions.JSONDecodeError:
        # Handle the case where the response isn't valid JSON
        print("Response content is not valid JSON")
elif response.status_code == 504:
    # Handle the 504 Gateway Timeout specifically
    print("Request failed with a 504 Gateway Timeout error.")
else:
    # Handle other possible HTTP errors
    print(f"Request failed with status code {response.status_code} and message: {response.text}")
