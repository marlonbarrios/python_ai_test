# 🚀 Deploy to Vercel - Step by Step Guide

## Method 1: Using Vercel CLI (Recommended)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```
This will open your browser to authenticate.

### Step 3: Set Environment Variable
```bash
vercel env add OPENAI_API_KEY production
```
When prompted, paste your OpenAI API key (from your `.env` file).

### Step 4: Deploy
```bash
vercel --prod
```

That's it! Your app will be deployed and you'll get a URL.

---

## Method 2: Using Vercel Dashboard (Easier - No CLI needed!)

### Step 1: Go to Vercel
1. Visit [vercel.com](https://vercel.com)
2. Sign up/Login with GitHub

### Step 2: Import Your Repository
1. Click "Add New..." → "Project"
2. Import your repository: `marlonbarrios/python_ai_test`
3. Click "Import"

### Step 3: Configure Project
- **Framework Preset:** Other (or leave default)
- **Root Directory:** `./` (default)
- **Build Command:** Leave empty (Vercel will auto-detect)
- **Output Directory:** Leave empty
- **Install Command:** Leave empty

### Step 4: Add Environment Variable
1. Click "Environment Variables"
2. Add new variable:
   - **Key:** `OPENAI_API_KEY`
   - **Value:** Your OpenAI API key (from `.env` file)
   - **Environment:** Production, Preview, Development (check all)
3. Click "Save"

### Step 5: Deploy
1. Click "Deploy"
2. Wait 2-3 minutes
3. Your app will be live! 🎉

---

## Your API Key
**Important:** Get your API key from your `.env` file and add it as an environment variable in Vercel!
Your API key should start with `sk-proj-` or `sk-`

---

## After Deployment

- Your app will be live at: `https://your-app-name.vercel.app`
- Vercel will automatically deploy on every git push
- Check the "Deployments" tab to see your app status

---

## Troubleshooting

- **Build fails:** Make sure `requirements.txt` is correct
- **API errors:** Verify `OPENAI_API_KEY` is set in Environment Variables
- **Import issues:** Make sure your GitHub repo is public or connected to Vercel

