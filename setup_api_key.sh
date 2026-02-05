#!/bin/bash

echo "🔑 OpenAI API Key Setup"
echo "========================"
echo ""
echo "You need to add your OpenAI API key to the .env file"
echo ""
echo "1. Get your API key from: https://platform.openai.com/api-keys"
echo "2. Copy your API key (it starts with 'sk-')"
echo ""
read -p "Enter your OpenAI API key: " api_key

if [ -z "$api_key" ]; then
    echo "❌ No API key provided. Exiting."
    exit 1
fi

# Update .env file
cat > .env << EOF
OPENAI_API_KEY=$api_key
PORT=5000
EOF

echo ""
echo "✅ API key saved to .env file!"
echo "🚀 You can now run: python app.py"

