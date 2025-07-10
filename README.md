Groq AI Chatbot

A high-performance conversational AI application built with Groq's inference engine and Gradio interface. This chatbot provides lightning-fast responses using state-of-the-art language models with a clean, professional web interface.
Overview

This project demonstrates the integration of Groq's optimized inference API with a user-friendly web interface. The application supports multiple advanced language models and provides real-time conversational capabilities with customizable parameters.
Features

    Multiple AI Models: Support for Llama3, Mixtral, and Gemma models

    Real-time Chat Interface: Interactive web-based conversation system

    Customizable Parameters: Adjustable temperature, system prompts, and model selection

    Conversation Management: Chat history, export functionality, and session clearing

    Professional UI: Clean, responsive design optimized for desktop and mobile

    Environment-based Configuration: Secure API key management through environment variables

Supported Models

    Llama3-8B-8192: Optimized for speed and efficiency

    Llama3-70B-8192: Enhanced reasoning capabilities for complex tasks

    Mixtral-8x7B-32768: Balanced performance across various use cases

    Gemma-7B-IT: Google's instruction-tuned model for diverse applications

Installation
Prerequisites

    Python 3.8 or higher

    Groq API key (obtain from console.groq.com)

Setup

    Clone the repository:

git clone https://github.com/yourusername/groq-chatbot.git
cd groq-chatbot

    Install dependencies:

pip install -r requirements.txt

    Set up environment variables:

export GROQ_API_KEY="your_groq_api_key_here"

Alternatively, create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

Usage
Local Development

Run the application locally:

python app.py

The interface will be available at http://localhost:7860
Google Colab

    Upload the notebook version

    Set your API key in the designated cell

    Run all cells to launch the interface

Configuration
Environment Variables

    GROQ_API_KEY: Required. Your Groq API key for authentication

Application Settings

    Temperature: Controls response randomness (0.0 to 2.0)

    Max Tokens: Maximum response length (configurable in code)

    System Prompt: Custom instructions for AI behavior

    Model Selection: Choose between available models

Project Structure

groq-chatbot/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .env                # Environment variables (optional)

Core Components
ChatbotConfig

Configuration management for the chatbot application.
GroqChatbot

Main chatbot class handling Groq API interactions and conversation management.

Key Methods:

    get_response(user_input): Generate AI response

    clear_history(): Reset conversation history

    change_model(model_name): Switch AI models

    set_temperature(temp): Adjust response creativity

Interface Functions

    chat_with_bot(): Primary chat handling function

    clear_chat(): Reset chat session

    export_chat(): Export conversation history

Development
Running Tests

python -m pytest tests/

Contributing

    Fork the repository

    Create a feature branch

git checkout -b feature/new-feature

Make your changes

Add tests for new functionality

Ensure all tests pass

Commit your changes

git commit -am 'Add new feature'

Push to the branch

    git push origin feature/new-feature

    Create a Pull Request

Performance

    Response Time: Sub-second response times with Groq's optimized inference

    Scalability: Handles multiple concurrent users

    Resource Usage: Minimal local resource requirements

Security

    API keys are handled through environment variables

    No sensitive data is stored in the application

    All communications use HTTPS when deployed

Limitations

    Requires active internet connection for API calls

    API usage is subject to Groq's rate limits and pricing

    Model availability depends on Groq's service status

Troubleshooting
Common Issues

API Key Not Found

    Ensure GROQ_API_KEY is set in environment variables

    Verify the API key is valid and active

Model Not Available

    Check Groq's service status

    Verify the model name is correct and supported

Installation Issues

    Update pip:

    pip install --upgrade pip

    Use a virtual environment for clean installation

License

This project is licensed under the MIT License.
Support

For issues and questions:

    Create an issue in the GitHub repository

    Check the Groq documentation

    Review the Gradio documentation

Changelog
Version 1.0.0

    Initial release with Groq API integration

    Gradio web interface implementation

    Multi-model support

    Basic conversation management

For more information about Groq's capabilities, visit groq.com
