# README.md

# DALL-E Node.js App

A Node.js application that generates images using OpenAI's DALL-E 3 model. Users can enter text descriptions and receive AI-generated images based on their prompts.

## Features

- OpenAI DALL-E 3 integration
- Real-time image generation
- Simple and responsive UI

## Project Structure

```
dalle-node-app/
├── src/
│   ├── app.js                # Express application entry point
│   ├── routes/
│   │   └── imageRoutes.js    # Image generation route handlers
│   ├── controllers/
│   │   └── imageController.js # DALL-E integration logic
│   └── public/
│       ├── index.html        # Main UI
│       ├── styles/
│       │   └── style.css     # Application styles
│       └── scripts/
│           └── main.js       # Frontend JavaScript
├── .env                      # Environment variables
├── .gitignore               # Git ignore rules
└── package.json             # Project configuration
```

## Prerequisites

- Node.js 14.x or higher
- npm or yarn
- OpenAI API key

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd dalle-node-app
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the root directory:
```plaintext
API_KEY=your_openai_api_key_here
```

4. Start the application:
```bash
npm start
```

5. Open your browser and visit `http://localhost:3000`

## Usage

1. Enter a descriptive prompt in the text input
2. Click "Generate Image"
3. Wait for the AI to generate your image
4. The generated image will appear below the input field

## License

MIT License