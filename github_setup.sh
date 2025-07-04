#!/bin/bash

# GitHub Repository Setup Script
echo "🚀 Setting up Reddit Comment Bot for GitHub..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Add files in organized commits
echo "📝 Creating organized commit history..."

# First commit: Core bot functionality
echo "💾 Commit 1/5: Core bot functionality..."
git add reddit_bot.py config.py requirements.txt .env.example
git commit -m "feat: add core Reddit bot functionality

- Implement main Reddit commenting bot (reddit_bot.py)
- Add comprehensive configuration system (config.py)
- Include Python dependencies (requirements.txt)
- Provide environment template (.env.example)"

# Second commit: Safety and utilities
echo "💾 Commit 2/5: Safety features and utilities..."
git add test_credentials.py utils.py
git commit -m "feat: add safety features and utility tools

- Add credential testing utility (test_credentials.py)
- Implement bot management tools (utils.py)
- Include comprehensive error handling and validation"

# Third commit: Setup and configuration
echo "💾 Commit 3/5: Setup and configuration..."
git add setup.sh comments.txt .gitignore
git commit -m "feat: add setup automation and configuration

- Automated installation script (setup.sh)
- Default comment templates (comments.txt)
- Comprehensive gitignore for security (.gitignore)"

# Fourth commit: Documentation
echo "💾 Commit 4/5: Documentation..."
git add README.md QUICKSTART.md CONTRIBUTING.md CHANGELOG.md LICENSE
git commit -m "docs: add comprehensive documentation

- Complete setup guide (README.md)
- Quick start instructions (QUICKSTART.md)
- Contributing guidelines (CONTRIBUTING.md)
- Version history (CHANGELOG.md)
- MIT license (LICENSE)"

# Fifth commit: GitHub integration
echo "💾 Commit 5/5: GitHub integration..."
git add .github/ github_setup.sh
git commit -m "ci: add GitHub integration and automation

- GitHub Actions CI/CD pipeline (.github/workflows/ci.yml)
- Repository setup automation (github_setup.sh)
- Security scanning and testing workflows"

echo "✅ All commits created successfully!"

echo ""
echo "📊 Commit history:"
git log --oneline

# Display next steps
echo ""
echo "🎉 Repository setup complete!"
echo ""
echo "Next steps to publish on GitHub:"
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: Reddit-Comment-Bot"
echo "   - Description: 🤖 Automated Reddit commenting bot for karma building"
echo "   - Make it Public (recommended) or Private"
echo "   - Don't initialize with README (we already have one)"
echo ""
echo "2. Connect and push to GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/Reddit-Comment-Bot.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Add repository topics/tags:"
echo "   reddit-bot, automation, python, praw, karma-farming,"
echo "   social-media-bot, reddit-api, comment-automation, rate-limiting"
echo ""
echo "📖 Repository Description:"
echo "🤖 Automated Reddit commenting bot for karma building - Responsibly post"
echo "comments across multiple subreddits with built-in rate limiting, smart post"
echo "filtering, and comprehensive safety features. Perfect for growing your Reddit"
echo "presence while following platform guidelines."
echo ""
echo "🔗 Useful GitHub features to enable:"
echo "- Issues (for bug reports and feature requests)"
echo "- Discussions (for community questions)"
echo "- Wiki (for extended documentation)"
echo "- Security advisories (for responsible disclosure)"
echo ""
echo "⚠️  Remember to:"
echo "- Never commit your .env file with real credentials"
echo "- Add appropriate GitHub repository topics"
echo "- Enable branch protection rules for main branch"
echo "- Consider adding a SECURITY.md file"

# Check if .env exists and warn about it
if [ -f ".env" ]; then
    echo ""
    echo "🔐 Security Check:"
    if git ls-files --error-unmatch .env 2>/dev/null; then
        echo "⚠️  WARNING: .env file is tracked by Git!"
        echo "   This could expose your Reddit credentials."
        echo "   Run: git rm --cached .env"
        echo "   Then commit the change."
    else
        echo "✅ .env file is properly ignored by Git"
    fi
fi

# Show current status
echo ""
echo "📊 Current repository status:"
git status --short

echo ""
echo "🎯 Ready to push to GitHub! 🚀"
