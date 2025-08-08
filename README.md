# 🤖 Reddit Comment Bot

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![PRAW](https://img.shields.io/badge/PRAW-7.8.1-orange.svg)](https://praw.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/Reddit-Comment-Bot.svg)](https://github.com/yourusername/Reddit-Comment-Bot/issues)

An intelligent Reddit commenting bot designed to help grow your karma responsibly. Features smart post filtering, rate limiting, and comprehensive safety measures to ensure compliance with Reddit's terms of service.

## ⚠️ **IMPORTANT DISCLAIMER**

This bot is for **educational purposes only**. Users must:
- ✅ Follow Reddit's [Terms of Service](https://www.redditinc.com/policies/user-agreement)
- ✅ Respect individual subreddit rules
- ✅ Use responsibly with appropriate delays
- ✅ Post meaningful, relevant comments
- ❌ **NOT** use for spam or malicious purposes

**Misuse of this bot may result in account suspension or banning.**

## ✨ Features

- 🎯 **Multi-subreddit targeting** - Comment across multiple communities
- 🛡️ **Built-in safety features** - Rate limiting, duplicate detection, post filtering
- 🧠 **Smart post selection** - Avoids old posts, own posts, heavily commented posts
- 🎲 **Random comment selection** - Customizable comment templates
- 📊 **Comprehensive logging** - Track all bot activity
- 🧪 **Dry-run mode** - Test without posting actual comments
- 🎮 **Interactive mode** - Manual control and monitoring
- ⚡ **Easy setup** - Automated installation and configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ and a Reddit account with API access

### Setup (5 minutes)
1. **Clone and install:**
   ```bash
   git clone https://github.com/yourusername/Reddit-Comment-Bot.git
   cd Reddit-Comment-Bot
   pip install -r requirements.txt
   ```

2. **Get Reddit API credentials:**
   - Visit [Reddit App Preferences](https://www.reddit.com/prefs/apps)
   - Create new app (type: "script")
   - Note your Client ID and Client Secret

3. **Configure:**
   ```bash
   cp .env.example .env
   # Edit .env with your Reddit credentials
   ```

4. **Test and run:**
   ```bash
   python3 test_credentials.py  # Verify setup
   python3 reddit_bot.py --dry-run --max-comments 2  # Safe test
   python3 reddit_bot.py --max-comments 3  # Live run (start small!)
   ```

📖 **For detailed setup instructions, see [QUICKSTART.md](QUICKSTART.md)**

## 🛡️ Safety Features

### Built-in Protections
- **Rate limiting** (30-120 second delays)
- **Post age filtering** (only recent posts)
- **Duplicate prevention** & **own post avoidance**
- **Score thresholds** & **comment limits per subreddit**

### Safety Controls
- **Dry-run mode** for testing
- **Interactive mode** for manual approval
- **Comprehensive logging** in `bot.log`

## 📖 Usage

### Command Options
```bash
python3 reddit_bot.py [OPTIONS]
  --dry-run              Test without posting
  --interactive          Manual control mode
  --max-comments N       Limit total comments
  --help                 Show help
```

### Configuration
- **`config.py`**: Target subreddits, rate limits, behavior settings
- **`comments.txt`**: Comment templates (one per line)
- **`.env`**: Reddit API credentials

### Monitoring
```bash
python3 utils.py --stats      # View statistics
python3 utils.py --activity   # Check recent activity
python3 utils.py --test       # Run diagnostics
```

## 🚨 Common Issues

| Issue | Solution |
|-------|----------|
| **401 Authentication Error** | Check credentials, ensure app type is "script" |
| **429 Rate Limited** | Increase delays, reduce comment frequency |
| **No suitable posts** | Lower score threshold, try different subreddits |

## 📝 Best Practices

1. **Start small** - Begin with 2-3 comments per session
2. **Quality first** - Use meaningful, relevant comments  
3. **Respect rules** - Follow each subreddit's guidelines
4. **Monitor actively** - Check logs and karma regularly
5. **Take breaks** - Don't run continuously

### Good vs. Bad Comments
✅ **Good**: "This is really insightful, thanks for sharing!"  
❌ **Avoid**: Generic responses like "Nice post"

## 🔧 Customization

### Adding Subreddits
Edit `TARGET_SUBREDDITS` in `config.py`:
```python
TARGET_SUBREDDITS = ['AskReddit', 'funny', 'YourFavoriteSubreddit']
```

### Rate Limiting
```python
# Conservative (safer)
RATE_LIMITS = {'min_delay': 60, 'max_delay': 300}

# More active (higher risk)
RATE_LIMITS = {'min_delay': 20, 'max_delay': 60}  # ⚠️ Use with caution
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License & Legal

Licensed under MIT License. See [LICENSE](LICENSE) for details.

**Legal Notice**: Users are responsible for compliance with Reddit's Terms of Service, subreddit rules, and local laws. This software is provided "as is" without warranty.

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/Reddit-Comment-Bot/issues)
- 💡 **Features**: [GitHub Discussions](https://github.com/yourusername/Reddit-Comment-Bot/discussions)
- 📖 **Quick Setup**: [QUICKSTART.md](QUICKSTART.md)

---
**Remember: Use this bot responsibly and follow Reddit's community guidelines!** 🤖✨
