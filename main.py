from flask import Flask, request, jsonify
# Flask class (Web framework), request (to handle incoming requests), jsonify (converts Python objects to JSON)

app = Flask(__name__) # Flask class instance

@app.route('/v1/chat/completions', methods=['POST']) # Maps the function to the URL. / POST = Data submission to a server
def fakeChatCompletion(): # Executed once a POST is made to the URL        
        print("Request recieved") # Debugging

        response = { # Mock response that a server returns once a POST is made.
            "id": "chatcmpl-123", # ID for each request
            "object": "chat.completion",  # Object type
            "created": 1677652288,  # Timestamp
            "model": "gpt-4o-mini",
            "system_fingerprint": "fp_44709d6fcb",  # identifier for the system
            
            "choices": [ # AI Assistant's response 
            {
                "index": 0, 
                "message": 
                {
                    "role": "assistant", 
                    "content": "Hello there, how may I assist you today?",
                    "finish_reason": "stop" # How the model stopped generating. "stop" = naturally
                }
            }],

            "usage": 
            { # Tokens = Words
                "prompt_tokens": 9, # Input
                "completion_tokens": 12, # Output
                "total_tokens": 21, 
            }
        }
        return jsonify(response) # response --> JSON, to be sent back to the client

if __name__ == '__main__':
    app.run(debug=True)

# NOTE: Typing the URL http://127.0.0.1:5000/v1/chat/completions is a GET request, which is not handled by the above code.
# To test the POST request, use Postman or the client py script.