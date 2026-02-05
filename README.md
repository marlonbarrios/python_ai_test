# AI Chatbot - Python Flask App

A simple, beautiful chatbot application built with Flask and OpenAI API. Deploy it easily to Vercel, Render, or any other platform.

## Features

- 🤖 Interactive chatbot interface
- 🎨 Modern, responsive UI
- 🔌 OpenAI API integration (GPT-4o-mini)
- 🚀 Ready for deployment

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Local Setup

### Step 1: Create a Virtual Environment (Recommended)

**Why use a virtual environment?**
- Keeps your project dependencies isolated from other Python projects
- Prevents version conflicts between different projects
- Makes your project portable and easier to deploy
- **This is a Python best practice!**

**Create and activate virtual environment:**

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

You'll know it's activated when you see `(venv)` at the start of your terminal prompt.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

1. Copy `env.example` to `.env`:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

   **Get your API key:** [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### Step 4: Run the App

```bash
python app.py
```

### Step 5: Open Your Browser

Navigate to `http://localhost:5000`

### Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment:
```bash
deactivate
```

**Note:** Always activate your virtual environment before running the app!

## Deployment Options

### Option 1: Deploy to Vercel (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Set environment variable:**
   ```bash
   vercel env add OPENAI_API_KEY
   ```
   (Enter your API key when prompted)

4. **Deploy:**
   ```bash
   vercel --prod
   ```

   Or connect your GitHub repository to Vercel for automatic deployments.

### Option 2: Deploy to Render

1. **Create a new account** at [render.com](https://render.com)

2. **Create a new Web Service:**
   - Connect your GitHub repository
   - Select "Python 3" as the environment
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

3. **Add environment variable:**
   - In the Render dashboard, go to Environment
   - Add `OPENAI_API_KEY` with your API key value

4. **Deploy:**
   - Render will automatically deploy your app

### Option 3: Deploy to Railway

1. **Create a new account** at [railway.app](https://railway.app)

2. **Create a new project** and connect your GitHub repository

3. **Add environment variable:**
   - Go to Variables
   - Add `OPENAI_API_KEY` with your API key value

4. **Deploy:**
   - Railway will automatically detect Python and deploy

### Option 4: Deploy to Fly.io

1. **Install Fly CLI:**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Login:**
   ```bash
   fly auth login
   ```

3. **Create app:**
   ```bash
   fly launch
   ```

4. **Set environment variable:**
   ```bash
   fly secrets set OPENAI_API_KEY=your-api-key-here
   ```

5. **Deploy:**
   ```bash
   fly deploy
   ```

## Configuration

### Changing the AI Model

Edit `app.py` and change the model in the `/chat` endpoint:

```python
model="gpt-4o-mini"  # Current model
# Options: "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo", etc.
```

### Adjusting Response Settings

You can modify these parameters in `app.py`:

- `max_tokens`: Maximum length of response (default: 500)
- `temperature`: Creativity level 0-1 (default: 0.7)

## Project Structure

```
python_aitest/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel configuration
├── templates/
│   └── index.html     # Chat interface
├── env.example        # Environment variables template
└── README.md         # This file
```

## Troubleshooting

- **"Module not found" error**: Make sure you've installed all dependencies with `pip install -r requirements.txt`
- **API errors**: Verify your OpenAI API key is correct and has credits
- **Port already in use**: Change the PORT in your `.env` file or kill the process using that port

## License

MIT License - feel free to use this project for your own purposes!

