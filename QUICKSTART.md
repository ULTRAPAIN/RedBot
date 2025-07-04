# 🚀 Quick Start Guide

## Reddit Bot Setup (5 minutes)

### Step 1: Get Reddit API Credentials
1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Fill in the form:
   - **Name**: Your bot name (e.g., "MyCommentBot")
   - **App type**: Select "script"
   - **Description**: Optional
   - **About URL**: Leave blank
   - **Redirect URI**: http://localhost:8080 (required but not used)
4. Click "Create app"
5. Note down:
   - **Client ID**: Found under the app name (short string)
   - **Client Secret**: The "secret" field (longer string)

### Step 2: Configure the Bot
1. Open the `.env` file in a text editor
2. Replace the placeholder values:
   ```
   REDDIT_CLIENT_ID=your_actual_client_id
   REDDIT_CLIENT_SECRET=your_actual_client_secret
   REDDIT_USER_AGENT=RedditBot/1.0 by YourUsername
   REDDIT_USERNAME=your_reddit_username
   REDDIT_PASSWORD=your_reddit_password
   ```

### Step 3: Customize Bot Behavior
Edit `config.py` to customize:
- **TARGET_SUBREDDITS**: List of subreddits to comment on
- **COMMENT_TEMPLATES**: Default comments (or use `comments.txt`)
- **Rate limits and delays**: To avoid being flagged as spam

### Step 4: Test the Bot
```bash
# Test without posting anything
python3 reddit_bot.py --dry-run

# Interactive mode for manual control
python3 reddit_bot.py --interactive

# Normal operation (start with low limits!)
python3 reddit_bot.py --max-comments 5
```

## ⚠️ Important Safety Tips

1. **Start Small**: Begin with `--max-comments 1` to test
2. **Use Delays**: Keep rate limits reasonable (30-120 seconds)
3. **Quality Comments**: Use meaningful, relevant comments
4. **Follow Rules**: Respect each subreddit's rules
5. **Monitor Logs**: Check `bot.log` for any issues

## 🛠 Troubleshooting

### "Failed to connect to Reddit"
- Check your credentials in `.env`
- Ensure your Reddit account can access the API
- Verify client ID and secret are correct

### "Rate limited"
- Increase delays in `config.py`
- Reduce comments per subreddit
- Wait before running again

### Comments not posting
- Check if subreddits allow new accounts to comment
- Verify your account has enough karma
- Check for subreddit-specific restrictions

## 📊 Monitoring

```bash
# View bot statistics
python3 utils.py --stats

# Check recent activity
python3 utils.py --activity

# Test configuration
python3 utils.py --test
```

## 🔧 Advanced Usage

### Custom Comment Lists
Create/edit `comments.txt` with one comment per line:
```
This is really interesting!
Great perspective on this topic.
Thanks for sharing this insight.
```

### Targeting Specific Subreddits
Edit `TARGET_SUBREDDITS` in `config.py`:
```python
TARGET_SUBREDDITS = [
    'AskReddit',
    'todayilearned',
    'YoutubeHaiku'
]
```

### Scheduling the Bot
Use cron to run automatically:
```bash
# Run every 2 hours
0 */2 * * * cd /path/to/Reddit_bot && python3 reddit_bot.py --max-comments 3
```

Remember: **Use responsibly and follow Reddit's Terms of Service!**
