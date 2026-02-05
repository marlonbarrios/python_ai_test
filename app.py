from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

app = Flask(__name__)
CORS(app)

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

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
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
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Call OpenAI API
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",  # Using a cost-effective model, can change to gpt-4o for better quality
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        assistant_message = response.choices[0].message.content
        
        return jsonify({
            'response': assistant_message
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")  # Debug print
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

