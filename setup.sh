#!/bin/bash

# Reddit Bot Setup Script
echo "🤖 Setting up Reddit Bot..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

echo "✅ Python and pip found"

# Install required packages
echo "📦 Installing Python packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Packages installed successfully"
else
    echo "❌ Failed to install packages"
    exit 1
fi

# Create .env file from template if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "🔧 IMPORTANT: Please edit the .env file with your Reddit API credentials!"
    echo "   1. Go to https://www.reddit.com/prefs/apps"
    echo "   2. Create a new app (choose 'script' type)"
    echo "   3. Fill in your credentials in the .env file"
    echo ""
else
    echo "✅ .env file already exists"
fi

# Create logs directory
mkdir -p logs

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your Reddit credentials"
echo "2. Customize config.py and comments.txt as needed"
echo "3. Run the bot:"
echo "   python3 reddit_bot.py --dry-run    (test mode)"
echo "   python3 reddit_bot.py --interactive (interactive mode)"
echo "   python3 reddit_bot.py              (normal mode)"
echo ""
echo "⚠️  Remember to use the bot responsibly and follow Reddit's terms of service!"
