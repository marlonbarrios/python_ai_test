#!/bin/bash

echo "🔧 Fixing dependency versions..."
echo ""

# Make sure we're in the virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Virtual environment not activated!"
    echo "   Run: source venv/bin/activate"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "📦 Uninstalling old versions..."
pip uninstall -y openai httpx 2>/dev/null || true

echo "📦 Installing compatible versions..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Dependencies fixed!"
echo "🚀 Now restart your app: python app.py"

