import requests

# Read the API key from a file
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

# Set up the API endpoint
api_endpoint = "https://api.openai.com/v1/completions"

# Set up the headers with your API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set up the payload (your question)
payload = {
    "model": "text-davinci-002",  # Model name
    "prompt": "How do I call ChatGPT via its API in Python?",  # Your question
    "max_tokens": 100  # Maximum number of tokens in the response
}

# Send the request to the API
response = requests.post(api_endpoint, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Get the response from the API
    data = response.json()
    # Extract the completion (response)
    completion = data["choices"][0]["text"]
    print(completion)
else:
    print("Failed to retrieve response from the API. Status code:", response.status_code)

