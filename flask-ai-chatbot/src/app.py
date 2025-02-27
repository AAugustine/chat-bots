from flask import Flask, render_template, request, jsonify
from src.services.openai_service import OpenAIService
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
openai_service = OpenAIService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def process_message():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Get response from OpenAI
        response = openai_service.get_chat_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)