from flask import Flask, request, jsonify, Response
# Flask class (Web framework), request (to handle incoming requests), jsonify (converts Python objects to JSON)
import logging, time # Debugging library / Response stream

logging.basicConfig(level=logging.INFO) # Set logging level/severity to INFO


app = Flask(__name__) # Flask class instance
@app.route('/v1/chat/completions', methods=['POST']) # Maps the function to the URL. / POST = Data submission to a server
def fakeChatCompletion(): # Executed once a POST is made to the URL        
        

        try:
            data = request.get_json() # Get the JSON data from the request body
            logging.info(f"Request: {data}") # Log the data

            # Validation for JSON keys
            REQUIRED_KEYS = {'model', 'messages'}
            OPTIONAL_KEYS = {"temperature", "top_p", "n", "stream", "stop",
            "max_tokens", "presence_penalty", "frequency_penalty",
            "logit_bias", "user", "seed"} # Most arent used, but are supported by the OpenAI API.
            ALLOWED_KEYS =  REQUIRED_KEYS | OPTIONAL_KEYS
            UNKNOWN_KEYS = set(data.keys()) - ALLOWED_KEYS
            if UNKNOWN_KEYS:
                return f"Invalid keys: {', '.join(UNKNOWN_KEYS)}", 400
            
        
            if 'model' not in data: # JSON validation
                 return "AI Model is missing.", 400
            if 'messages' not in data:
                 return "A message is missing.", 400
            if 'temperature' not in data:
                 return "Randomness not identified.", 400
            
            if len(data['messages']) == 0: # Message validation
                return "Prompt shouldn't be empty.", 400


            if data.get("stream", False): # If true, streams data.
                def generateStream():
                # Yield = stream chunk, prefixed  `data: `
                 yield 'data: {"id":"chatcmpl-123","choices":[{"delta":{"role":"assistant"},"index":0}]}\n\n'
                 yield 'data: {"choices":[{"delta":{"content":"Hello"},"index":0}]}\n\n'
                 time.sleep(0.3)
                 yield 'data: {"choices":[{"delta":{"content":" there"},"index":0}]}\n\n'
                 time.sleep(0.3)
                 yield 'data: {"choices":[{"delta":{"content":"!"},"index":0}]}\n\n'
                 yield 'data: [DONE]\n\n'
                 return Response(generateStream(), content_type='text/event-stream')
        
            response = { # Server mock response JSON, returned from a client's POST request.
                "id": "chatcmpl-123", # ID for each request
                "object": "chat.completion",  # Object type
                "created": 1677652288,  # Timestamp
                "model": "gpt-4o-mini",
                "system_fingerprint": "fp_44709d6fcb",  # Identifier for the system
                
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
       
        except Exception as e:
            logging.error("An unexpected error has occured: " + str(e)) 
            return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)

# NOTE: Typing the URL http://127.0.0.1:5000/v1/chat/completions is a GET request, which is not handled by the above code.
# To test the POST request, use Postman or the client py script once the server is running.