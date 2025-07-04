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

- Python 3.7 or higher
- A Reddit account
- Reddit API credentials (free)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Reddit-Comment-Bot.git
cd Reddit-Comment-Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the automated setup:

```bash
chmod +x setup.sh
./setup.sh
```

### 3. Get Reddit API Credentials

#### Step-by-Step Guide:

1. **Go to Reddit Apps**: Visit [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

2. **Login**: Sign in to your Reddit account

3. **Create New App**:
   - Click **"Create App"** or **"Create Another App"**
   - Fill in the form:
     - **Name**: `MyRedditBot` (or any name you prefer)
     - **App type**: **Select "script"** ⚠️ *This is crucial!*
     - **Description**: Optional
     - **About URL**: Leave blank
     - **Redirect URI**: `http://localhost:8080`

4. **Submit**: Click **"Create app"**

5. **Get Your Credentials**: After creation, you'll see:
   ```
   ┌─────────────────────────────────────┐
   │ MyRedditBot                         │
   │ personal use script by YourUsername │
   │                                     │
   │ AbCdEf12345678  ← CLIENT_ID        │
   │ secret: AbCdE...901  ← SECRET      │
   │ [edit] [delete]                     │
   └─────────────────────────────────────┘
   ```

### 4. Configure the Bot

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```bash
# Reddit API Credentials
REDDIT_CLIENT_ID=your_client_id_from_step_5
REDDIT_CLIENT_SECRET=your_client_secret_from_step_5
REDDIT_USER_AGENT=RedditBot/1.0 by YourUsername
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# Bot Configuration
MIN_DELAY=30
MAX_DELAY=120
MAX_COMMENTS_PER_SUBREDDIT=5
```

### 5. Test Your Setup

Test your credentials:

```bash
python3 test_credentials.py
```

Expected output:
```
🔐 Reddit Credential Tester
========================================
✅ REDDIT_CLIENT_ID: AbCdEf12345678
✅ REDDIT_CLIENT_SECRET: ***************
✅ All credentials found! Testing connection...
🎉 SUCCESS! Connected as: YourUsername
```

### 6. Run the Bot

**Safe testing (recommended first):**
```bash
# Dry run - no actual comments posted
python3 reddit_bot.py --dry-run --max-comments 2

# Interactive mode for manual control
python3 reddit_bot.py --interactive
```

**Live operation (start small!):**
```bash
# Start with just 3 comments
python3 reddit_bot.py --max-comments 3

# Normal operation
python3 reddit_bot.py
```

## 📖 Usage Guide

### Command Line Options

```bash
python3 reddit_bot.py [OPTIONS]

Options:
  --dry-run              Test without posting comments
  --interactive          Run in interactive mode
  --max-comments N       Limit total comments to N
  --help                 Show help message
```

### Configuration Files

#### `config.py` - Main Configuration
```python
# Target subreddits (without 'r/' prefix)
TARGET_SUBREDDITS = [
    'AskReddit',
    'funny',
    'todayilearned',
    # Add your preferred subreddits
]

# Comment behavior
COMMENT_BEHAVIOR = {
    'max_retries': 3,
    'avoid_own_posts': True,
    'avoid_already_commented': True,
}

# Rate limiting
RATE_LIMITS = {
    'min_delay': 30,  # Minimum seconds between comments
    'max_delay': 120, # Maximum seconds between comments
}
```

#### `comments.txt` - Comment Templates
Add one comment per line:
```
This is really interesting!
Great perspective on this topic.
Thanks for sharing this insight.
I learned something new today.
```

### Monitoring and Management

#### View Statistics
```bash
python3 utils.py --stats
```

#### Check Recent Activity
```bash
python3 utils.py --activity
```

#### Backup Data
```bash
python3 utils.py --backup
```

## 🛡️ Safety Features

### Automatic Protections

- **Rate Limiting**: 30-120 second delays between comments
- **Post Age Filter**: Only comments on recent posts (< 24 hours)
- **Duplicate Prevention**: Tracks previously commented posts
- **Own Post Avoidance**: Never comments on your own posts
- **Score Threshold**: Only comments on posts with minimum upvotes
- **Comment Limit**: Maximum comments per subreddit per run

### Manual Safety Controls

- **Dry Run Mode**: Test everything without posting
- **Interactive Mode**: Manual approval for each action
- **Comprehensive Logging**: Track all bot activity
- **Easy Monitoring**: View stats and recent activity

## 📊 Understanding the Logs

The bot creates detailed logs in `bot.log`:

```log
2025-07-04 16:34:45,218 - RedditBot - INFO - ✅ Successfully connected as u/YourUsername
2025-07-04 16:34:45,835 - RedditBot - INFO - [DRY RUN] Would comment on 'Post Title...' in r/AskReddit
2025-07-04 16:34:45,835 - RedditBot - INFO - [DRY RUN] Comment: Great post! Thanks for sharing.
```

### Log Levels:
- **INFO**: Normal operations
- **WARNING**: Non-critical issues
- **ERROR**: Problems that need attention

## 🔧 Customization

### Adding New Subreddits

Edit `config.py`:
```python
TARGET_SUBREDDITS = [
    'AskReddit',
    'funny',
    'YourFavoriteSubreddit',  # Add here
]
```

### Custom Comments

Edit `comments.txt` or modify `COMMENT_TEMPLATES` in `config.py`:
```python
COMMENT_TEMPLATES = [
    "Your custom comment here",
    "Another thoughtful response",
    "Engaging question or observation",
]
```

### Adjusting Behavior

#### More Conservative (Safer):
```python
RATE_LIMITS = {
    'min_delay': 60,   # Longer delays
    'max_delay': 300,
}

POST_SELECTION = {
    'min_score': 50,   # Higher score threshold
    'max_comments': 100,  # Fewer comments limit
}
```

#### More Active (Higher Risk):
```python
RATE_LIMITS = {
    'min_delay': 20,   # Shorter delays
    'max_delay': 60,
}

# ⚠️ Use with caution!
```

## 🚨 Troubleshooting

### Common Issues

#### 401 Authentication Error
```
❌ Failed to connect to Reddit: received 401 HTTP response
```

**Solutions:**
- ✅ Check username and password are correct
- ✅ Verify CLIENT_ID and CLIENT_SECRET
- ✅ Ensure app type is set to "script"
- ✅ Disable 2FA on Reddit account

#### Rate Limited
```
❌ received 429 HTTP response
```

**Solutions:**
- ⏱️ Wait 10-15 minutes before trying again
- 📉 Increase delays in `config.py`
- 📊 Reduce comments per subreddit

#### No Suitable Posts Found
```
⚠️ No suitable posts found in r/subreddit
```

**Solutions:**
- 📅 Check if posts are too old (adjust `max_age_hours`)
- 📊 Lower the `min_score` threshold
- 🎯 Try different subreddits

### Getting Help

1. **Check the logs**: `tail -f bot.log`
2. **Test credentials**: `python3 test_credentials.py`
3. **Run diagnostics**: `python3 utils.py --test`
4. **Use dry-run mode**: `python3 reddit_bot.py --dry-run`

## 📝 Best Practices

### Responsible Usage

1. **Start Small**: Begin with 2-3 comments per session
2. **Quality Over Quantity**: Use meaningful, relevant comments
3. **Monitor Response**: Watch your karma and adjust if needed
4. **Respect Communities**: Read and follow subreddit rules
5. **Regular Breaks**: Don't run the bot continuously

### Comment Guidelines

✅ **Good Comments:**
- "This is really insightful, thanks for sharing!"
- "I never thought about it that way before."
- "Great explanation, very helpful!"

❌ **Avoid:**
- Generic responses like "Nice post"
- Completely irrelevant comments
- Promotional or spam content

### Scheduling

Use cron for automated runs:
```bash
# Run every 2 hours with 3 comments max
0 */2 * * * cd /path/to/Reddit-Comment-Bot && python3 reddit_bot.py --max-comments 3
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Development Setup

```bash
git clone https://github.com/yourusername/Reddit-Comment-Bot.git
cd Reddit-Comment-Bot
pip install -r requirements.txt
cp .env.example .env
# Configure your .env file
python3 test_credentials.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Legal Notice

This software is provided "as is" without warranty. Users are responsible for compliance with:
- Reddit's Terms of Service
- Individual subreddit rules
- Local laws and regulations

The authors are not responsible for any misuse or consequences of using this software.

## 🙏 Acknowledgments

- [PRAW](https://praw.readthedocs.io/) - Python Reddit API Wrapper
- Reddit API for providing the platform
- The open-source community for inspiration and tools

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/Reddit-Comment-Bot/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/yourusername/Reddit-Comment-Bot/discussions)
- 📖 **Documentation**: See [QUICKSTART.md](QUICKSTART.md) for rapid setup

---

**Remember: Use this bot responsibly and always follow Reddit's community guidelines!** 🤖✨
