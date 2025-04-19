import requests # HTTP requests 

URL = "http://127.0.0.1:5000/v1/chat/completions" # Same endpoint as the server

payload = { # The request body, similar to what OpenAI API would recieve.
    "model": "gpt-4o-mini",
    "messages": 
    [        
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
        ],
    "temperature": 0.7, # Controls randomness in the output. 0 = deterministic, 1 = random
    "stream": False, # If True, the response will be streamed back in chunks
}

response = requests.post(URL, json=payload) # Sends post request to the server and will contain the server's output.
print("Status Code: ",response.status_code)  # Print the status code of the response
print("Response JSON:",response.json())  # Print the JSON response from the server

# Both the client and server should be running at the same time for this to work.
# The client and server have static, scripted responses. A real OpenAI API would have dynamic responses based on the input.
# The server is a mockup and does not perform any actual AI processing. It simply returns a predefined response with appropriate formatting.