import ollama

def get_response(message):
    try:
        # Ensure the message is within the 2000-character limit
        if len(message) > 2000:
            return "Error: Message exceeds 2000-character limit."

        response = ollama.chat(model='smollm:135m', messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":  message}
        ])
        
        # Ensure the response is within the 2000-character limit
        response_message = response.get("message", {}).get("content", "No response received.")
        
        
    except Exception as e:
        return f"Error: {str(e)}"
    
    return response_message
