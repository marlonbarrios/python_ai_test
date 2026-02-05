from flask import Flask, request, jsonify, render_template, Response, stream_with_context
from flask_cors import CORS
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

app = Flask(__name__)
CORS(app)

# Available models
AVAILABLE_MODELS = {
    "gpt-4o": {"name": "GPT-4o", "description": "Most capable model"},
    "gpt-4o-mini": {"name": "GPT-4o Mini", "description": "Fast and affordable"},
    "gpt-4-turbo": {"name": "GPT-4 Turbo", "description": "High performance"},
    "gpt-3.5-turbo": {"name": "GPT-3.5 Turbo", "description": "Fast and efficient"}
}

# Initialize OpenAI client (lazy initialization to avoid errors)
api_key = os.getenv('OPENAI_API_KEY')
client = None

def get_client():
    """Get or create OpenAI client"""
    global client
    if client is None:
        if not api_key or api_key == 'your_openai_api_key_here':
            return None
        try:
            client = OpenAI(api_key=api_key)
        except Exception as e:
            print(f"⚠️  Error initializing OpenAI client: {e}")
            return None
    return client

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/models', methods=['GET'])
def get_models():
    """Get available models"""
    return jsonify(AVAILABLE_MODELS)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests with conversation history"""
    try:
        # Get client (lazy initialization)
        openai_client = get_client()
        if not openai_client:
            return jsonify({
                'error': 'OpenAI API key is not configured. Please set OPENAI_API_KEY in your .env file with your actual API key.'
            }), 500
        
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
            
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])  # Get conversation history
        model = data.get('model', 'gpt-4o-mini')
        temperature = data.get('temperature', 0.7)
        max_tokens = data.get('max_tokens', 1000)
        stream = data.get('stream', False)
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Validate model
        if model not in AVAILABLE_MODELS:
            model = 'gpt-4o-mini'
        
        # Build messages array with system prompt and history
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        
        # Add conversation history (last 20 messages to avoid token limits)
        for msg in conversation_history[-20:]:
            if msg.get('role') and msg.get('content'):
                messages.append({
                    "role": msg['role'],
                    "content": msg['content']
                })
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        if stream:
            # Streaming response
            def generate():
                try:
                    stream_response = openai_client.chat.completions.create(
                        model=model,
                        messages=messages,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        stream=True
                    )
                    
                    for chunk in stream_response:
                        if chunk.choices[0].delta.content:
                            yield f"data: {json.dumps({'content': chunk.choices[0].delta.content})}\n\n"
                    
                    yield "data: [DONE]\n\n"
                except Exception as e:
                    yield f"data: {json.dumps({'error': str(e)})}\n\n"
            
            return Response(stream_with_context(generate()), mimetype='text/event-stream')
        else:
            # Non-streaming response
            response = openai_client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            assistant_message = response.choices[0].message.content
            
            return jsonify({
                'response': assistant_message
            })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Check API key on startup
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("⚠️  WARNING: OPENAI_API_KEY is not set or is using placeholder value!")
        print("⚠️  Please set your OpenAI API key in the .env file")
        print("⚠️  The app will start but chat functionality will not work.")
    
    port = int(os.getenv('PORT', 5000))
    print(f"\n🚀 Server starting on http://localhost:{port}")
    print("📝 Open this URL in your browser\n")
    app.run(host='0.0.0.0', port=port, debug=True)

