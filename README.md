# Health Buddy - AI Health Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-orange.svg)](https://groq.com/)

An intelligent AI-powered health assistant chatbot that provides accessible health advice and guidance using advanced natural language processing. Built with Flask and powered by Groq's LLaMA 3.1 model.

## ⚠️ Important Disclaimer

**This application is for informational purposes only and does not replace professional medical advice, diagnosis, or treatment.** Always consult with qualified healthcare providers for medical concerns. The AI responses are generated based on general medical knowledge and should not be considered as personalized medical recommendations.

## Overview

Health Buddy is a web-based AI chatbot designed to make health advice more accessible. It uses conversational AI to provide users with:
- General health information and guidance
- Symptom analysis suggestions
- Lifestyle and dietary recommendations
- Wellness tips and preventive care advice

The application maintains conversation history and provides empathetic, professional responses while strictly focusing on health-related topics.

## Features

### 🤖 AI-Powered Conversations
- Powered by Groq's LLaMA 3.1-8B model for fast, accurate responses
- Maintains conversation context and history
- Empathetic and professional tone

### 🏥 Health-Focused Assistance
- Symptom analysis and possible causes
- General medical suggestions
- Diet and lifestyle recommendations
- Preventive health tips

### 💬 Interactive Web Interface
- Modern, responsive chat interface
- Real-time message exchange
- Clean, accessible design with dark theme
- Mobile-friendly responsive layout

### 🔒 Privacy & Safety
- Client-side conversation management
- No personal health data storage
- Strict focus on health topics only
- Built-in safety disclaimers

### 🛠️ Developer-Friendly
- RESTful API endpoints
- Session-based conversation management
- Easy deployment with Flask
- Environment variable configuration

## Project Structure

```
health-buddy/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── templates/
│   └── index.html        # Main web interface
├── static/               # Static assets (CSS, JS, images)
├── .venv/                # Virtual environment
└── README.md            # Project documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- A Groq API key (sign up at [groq.com](https://groq.com))

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Serero-Codes/AI-Chatbot.git
   cd AI-Chatbot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   FLASK_SECRET_KEY=your_secret_key_here
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the chatbot:**
   Open your browser and navigate to `http://localhost:5000`

## Usage

### Web Interface
1. Open the application in your browser
2. Start a conversation by typing your health-related question
3. The AI will respond with relevant health information and guidance
4. Continue the conversation for follow-up questions

### API Endpoints

#### POST `/chat`
Send a message to the chatbot.

**Request Body:**
```json
{
  "message": "I have a headache and feel tired"
}
```

**Response:**
```json
{
  "reply": "I'm sorry to hear you're not feeling well. Headaches can have many causes...",
  "status": "ok"
}
```

#### POST `/reset`
Clear the conversation history.

**Response:**
```json
{
  "status": "ok",
  "message": "Conversation reset."
}
```

#### GET `/history`
Retrieve the conversation history.

**Response:**
```json
{
  "history": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help you with your health today?"}
  ]
}
```

## Key Components

### Backend (Flask Application)
- **Conversation Management:** Uses Flask sessions to maintain chat history
- **AI Integration:** Interfaces with Groq API for natural language processing
- **Response Formatting:** Ensures clean, readable AI responses
- **Safety Controls:** Enforces health-focused conversations only

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design:** Works on desktop and mobile devices
- **Real-time Chat:** AJAX-based message sending and receiving
- **Modern UI:** Dark theme with gradient accents and smooth animations
- **Accessibility:** Proper semantic HTML and keyboard navigation

### AI Model Configuration
- **Model:** LLaMA 3.1-8B Instant (via Groq)
- **Temperature:** 0.7 for balanced creativity and accuracy
- **Max Tokens:** 1024 for comprehensive responses
- **System Prompt:** Comprehensive health-focused instructions

## Examples

### Sample Conversation

**User:** I'm feeling very tired and have been having headaches for the past few days.

**Health Buddy:** I'm sorry to hear you're experiencing fatigue and headaches. These symptoms can have several possible causes. Let me help you understand this better.

Could you tell me:
- How long have the headaches been occurring?
- What does the headache feel like (throbbing, constant, etc.)?
- Have you noticed any other symptoms?
- How is your sleep and daily routine?

This information will help me provide more relevant general health suggestions.

### API Usage Example

```python
import requests

# Send a message
response = requests.post('http://localhost:5000/chat',
                        json={'message': 'What are some healthy breakfast ideas?'})

print(response.json()['reply'])
```

## Development

### Running in Debug Mode
```bash
export FLASK_ENV=development
python app.py
```

### Testing the API
```bash
# Test chat endpoint
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello"}'
```

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes

## Contributing

We welcome contributions to improve Health Buddy! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Ensure all changes maintain the health-focused scope
- Test thoroughly before submitting
- Update documentation as needed
- Follow the existing code style

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Serero Codes** - *Initial development* - [GitHub](https://github.com/Serero-Codes)

## Acknowledgments

- **Groq** for providing fast AI inference
- **Flask** for the web framework
- **LLaMA 3.1** for the underlying AI model
- Medical professionals who inspire responsible AI health applications

---

**Remember:** This AI assistant is designed to provide general health information and should not be used as a substitute for professional medical advice. Always consult healthcare professionals for medical concerns.