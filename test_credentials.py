#!/usr/bin/env python3
"""
Reddit Credential Tester
Test your Reddit API credentials before running the bot.
"""

import os
import sys
import praw
from dotenv import load_dotenv

def test_credentials():
    """Test Reddit API credentials step by step."""
    print("🔐 Reddit Credential Tester")
    print("=" * 40)
    
    # Load environment variables
    load_dotenv()
    
    # Check if credentials are filled
    credentials = {
        'REDDIT_CLIENT_ID': os.getenv('REDDIT_CLIENT_ID'),
        'REDDIT_CLIENT_SECRET': os.getenv('REDDIT_CLIENT_SECRET'),
        'REDDIT_USER_AGENT': os.getenv('REDDIT_USER_AGENT'),
        'REDDIT_USERNAME': os.getenv('REDDIT_USERNAME'),
        'REDDIT_PASSWORD': os.getenv('REDDIT_PASSWORD')
    }
    
    print("📋 Checking .env file...")
    
    missing_or_placeholder = []
    for key, value in credentials.items():
        if not value or 'your_' in value.lower() or 'here' in value.lower():
            missing_or_placeholder.append(key)
            print(f"❌ {key}: Missing or placeholder value")
        else:
            # Mask sensitive info for display
            if 'PASSWORD' in key or 'SECRET' in key:
                display_value = value[:3] + '*' * (len(value) - 6) + value[-3:] if len(value) > 6 else '*' * len(value)
            else:
                display_value = value
            print(f"✅ {key}: {display_value}")
    
    if missing_or_placeholder:
        print(f"\n❌ Found {len(missing_or_placeholder)} missing credentials!")
        print("\n📖 How to get your credentials:")
        print("1. Go to: https://www.reddit.com/prefs/apps")
        print("2. Click 'Create App' or 'Create Another App'")
        print("3. Choose 'script' as app type")
        print("4. Fill in a name and redirect URI: http://localhost:8080")
        print("5. After creating, you'll see:")
        print("   • CLIENT_ID: 14-character string under app name")
        print("   • CLIENT_SECRET: 27-character string after 'secret:'")
        print("6. Update your .env file with these values")
        return False
    
    print(f"\n✅ All credentials found! Testing connection...")
    
    # Test Reddit connection
    try:
        reddit = praw.Reddit(
            client_id=credentials['REDDIT_CLIENT_ID'],
            client_secret=credentials['REDDIT_CLIENT_SECRET'],
            user_agent=credentials['REDDIT_USER_AGENT'],
            username=credentials['REDDIT_USERNAME'],
            password=credentials['REDDIT_PASSWORD']
        )
        
        # Test by getting user info
        user = reddit.user.me()
        print(f"🎉 SUCCESS! Connected as: {user.name}")
        print(f"📊 Account karma: {user.comment_karma + user.link_karma}")
        print(f"📅 Account created: {user.created_utc}")
        
        # Test subreddit access
        try:
            test_sub = reddit.subreddit('test')
            print(f"🔍 Can access subreddits: ✅")
        except Exception as e:
            print(f"⚠️  Subreddit access warning: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        
        # Provide specific error help
        error_str = str(e).lower()
        if '401' in error_str:
            print("\n🔍 401 Error means:")
            print("• Wrong username/password")
            print("• Wrong client ID/secret")
            print("• App not set to 'script' type")
        elif '403' in error_str:
            print("\n🔍 403 Error means:")
            print("• Account may be suspended")
            print("• App permissions issue")
        elif 'too many requests' in error_str:
            print("\n🔍 Rate limit error:")
            print("• Wait a few minutes and try again")
        
        return False

def interactive_setup():
    """Interactive credential setup."""
    print("\n🛠️  Interactive Credential Setup")
    print("=" * 40)
    
    print("Let's set up your Reddit credentials step by step...")
    print("\nFirst, go to: https://www.reddit.com/prefs/apps")
    print("and create a new 'script' type app.")
    
    input("\nPress Enter when you've created your Reddit app...")
    
    # Get credentials interactively
    print("\nEnter your Reddit app credentials:")
    
    client_id = input("CLIENT_ID (14-character string): ").strip()
    client_secret = input("CLIENT_SECRET (27-character string): ").strip()
    username = input("Reddit username: ").strip()
    password = input("Reddit password: ").strip()
    user_agent = f"RedditBot/1.0 by {username}"
    
    # Update .env file
    env_content = f"""# Reddit Bot Configuration
# Automatically generated credentials

# Reddit API Credentials (Get these from https://www.reddit.com/prefs/apps)
REDDIT_CLIENT_ID={client_id}
REDDIT_CLIENT_SECRET={client_secret}
REDDIT_USER_AGENT={user_agent}
REDDIT_USERNAME={username}
REDDIT_PASSWORD={password}

# Bot Configuration
MIN_DELAY=30  # Minimum delay between comments (seconds)
MAX_DELAY=120  # Maximum delay between comments (seconds)
MAX_COMMENTS_PER_SUBREDDIT=5  # Maximum comments per subreddit per run
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("\n✅ Credentials saved to .env file!")
        
        # Test the credentials
        print("\n🧪 Testing credentials...")
        if test_credentials():
            print("\n🎉 Setup complete! You can now run the bot.")
        else:
            print("\n❌ Setup failed. Please check your credentials.")
            
    except Exception as e:
        print(f"\n❌ Error saving credentials: {e}")

def main():
    if not os.path.exists('.env'):
        print("📄 No .env file found. Starting interactive setup...")
        interactive_setup()
    else:
        success = test_credentials()
        if not success:
            setup = input("\n🔧 Would you like to run interactive setup? (y/n): ").lower()
            if setup == 'y':
                interactive_setup()

if __name__ == "__main__":
    main()
