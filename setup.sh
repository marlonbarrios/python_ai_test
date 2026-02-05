#!/bin/bash

# Setup script for AI Chatbot
echo "🚀 Setting up AI Chatbot..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Virtual environment created!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "Then install dependencies with:"
echo "  pip install -r requirements.txt"
echo ""
echo "Don't forget to:"
echo "  1. Copy env.example to .env"
echo "  2. Add your OpenAI API key to .env"
echo "  3. Run: python app.py"

