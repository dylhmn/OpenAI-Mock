from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST']) # Associates the function and URL / POST = Data submission to a server
def fakeChatCompletion():
        print("Request recieved")


        response = {
            "id": "chatcmpl-123", 
            "object": "chat.completion", 
            "created": 1677652288,  # mock timestamp, can be generated dynamically
            "model": "gpt-4o-mini",  # mock model
            "system_fingerprint": "fp_44709d6fcb",  # mock fingerprint
            "choices": [{
                "index": 0, 
                "message": {
                    "role": "assistant", 
                    "content": "Hello there, how may I assist you today?", 
                    "logprobs": None,  # this can be null, or you can fake it
                    "finish_reason": "stop" 
                }
            }],
            "usage": {
                "prompt_tokens": 9, 
                "completion_tokens": 12, 
                "total_tokens": 21, 
                "completion_tokens_details": {
                    "reasoning_tokens": 0  # example of detailed usage info
                }
            }
        }

        return jsonify(response)
