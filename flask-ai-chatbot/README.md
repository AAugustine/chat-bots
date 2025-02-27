# README.md

# Flask AI Chatbot

This project is a Flask-based AI Chatbot that integrates with the OpenAI API. It allows users to interact with the chatbot through a web interface and receive responses powered by OpenAI's language model with some fun twists on responses.

## Project Structure

```
flask-ai-chatbot
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── templates
│   │   ├── base.html         # Base template for the application
│   │   ├── chat.html         # Template for the chat interface
│   │   └── index.html        # Landing page template
│   ├── static
│   │   ├── css
│   │   │   └── styles.css    # CSS styles for the application
│   │   └── js
│   │       └── chat.js       # JavaScript for chat interactions
│   ├── services
│   │   └── openai_service.py  # Service for interacting with the OpenAI API
│   └── utils
│       └── helpers.py        # Utility functions
├── tests
│   ├── test_app.py           # Unit tests for the app.py file
│   └── test_openai_service.py # Unit tests for the openai_service.py file
├── .env                       # Environment variables
├── .gitignore                 # Git ignore file
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd flask-ai-chatbot
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

To run the Flask application, execute the following command:
```
python src/app.py
```

## Testing

To run the tests, make sure you have pytest installed:

```bash
pip install pytest
```

Run all tests: `python -m pytest tests/ -v`

Run specific test files:

```bash
# Run app tests
python -m pytest tests/test_app.py -v

# Run OpenAI service tests
python -m pytest tests/test_openai_service.py -v
```

Run tests with debug output:
```bash
python -m pytest tests/ -v -s
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.