#!/usr/bin/env python3
"""
Simple script to check setup and run the app
"""
import os
import sys

def check_setup():
    """Check if everything is set up correctly"""
    print("🔍 Checking setup...")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("   Run: cp env.example .env")
        print("   Then edit .env and add your OPENAI_API_KEY")
        return False
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Virtual environment might not be activated")
        print("   Run: source venv/bin/activate")
        print("   (Continuing anyway...)\n")
    
    # Check if required packages are installed
    try:
        import flask
        import openai
        print("✅ Required packages are installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    print("✅ Setup looks good!\n")
    return True

if __name__ == '__main__':
    if check_setup():
        print("🚀 Starting Flask app...")
        print("📝 Open http://localhost:5000 in your browser\n")
        from app import app
        port = int(os.getenv('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        print("\n❌ Please fix the issues above before running the app")
        sys.exit(1)

