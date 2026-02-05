#!/bin/bash

echo "🚀 Deploying to Vercel"
echo "======================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed."
    echo "   Install it from: https://nodejs.org/"
    exit 1
fi

# Install Vercel CLI if not installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
fi

echo ""
echo "🔐 Step 1: Login to Vercel"
echo "   (This will open a browser for authentication)"
vercel login

echo ""
echo "🔑 Step 2: Setting environment variable"
echo "   Enter your OpenAI API key when prompted:"
vercel env add OPENAI_API_KEY production

echo ""
echo "🚀 Step 3: Deploying to production..."
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo "   Your app should be live at the URL shown above"

