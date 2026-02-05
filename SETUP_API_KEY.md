# How to Set Up Your OpenAI API Key

## Quick Setup (Choose One Method)

### Method 1: Using the Setup Script (Easiest)

Run this command in your terminal:
```bash
./setup_api_key.sh
```

Then enter your API key when prompted.

### Method 2: Manual Setup

1. **Get your API key:**
   - Go to https://platform.openai.com/api-keys
   - Sign in or create an account
   - Click "Create new secret key"
   - Copy the key (it starts with `sk-`)

2. **Edit the .env file:**
   
   **Option A - Using nano (terminal editor):**
   ```bash
   nano .env
   ```
   - Replace `your_openai_api_key_here` with your actual key
   - Press `CTRL+X`, then `Y`, then `ENTER` to save

   **Option B - Using VS Code or your editor:**
   ```bash
   code .env
   ```
   Or just open `.env` in your editor and edit it.

3. **Your .env file should look like this:**
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   PORT=5000
   ```
   
   **Important:** 
   - Replace the entire `your_openai_api_key_here` with your actual key
   - Don't add quotes around the key
   - Make sure there are no extra spaces

4. **Restart your app:**
   ```bash
   python app.py
   ```

## Verify It's Working

After setting up your API key:
1. Make sure your virtual environment is activated (`source venv/bin/activate`)
2. Restart the Flask app (`python app.py`)
3. Try sending a message in the chatbot
4. If you see an error, check that your API key is correct and has credits

## Troubleshooting

- **"API key is not configured"**: Your .env file still has the placeholder. Make sure you replaced `your_openai_api_key_here` with your actual key.
- **"Invalid API key"**: Double-check that you copied the entire key correctly (it should start with `sk-`)
- **"Insufficient credits"**: Your OpenAI account needs to have credits. Add billing info at https://platform.openai.com/account/billing

