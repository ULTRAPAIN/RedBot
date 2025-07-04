#!/usr/bin/env python3
"""
Reddit Bot - Automated Comment Bot
A responsible Reddit bot that can post comments across multiple communities.

Usage:
    python reddit_bot.py [options]

Options:
    --dry-run       Test the bot without actually posting comments
    --interactive   Run in interactive mode for manual control
    --help         Show this help message
"""

import praw
import random
import time
import logging
import os
import sys
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv
from typing import List, Dict, Optional
import json

# Import configuration
from config import (
    TARGET_SUBREDDITS, COMMENT_TEMPLATES, POST_SELECTION, 
    COMMENT_BEHAVIOR, RATE_LIMITS, LOGGING
)

class RedditBot:
    def __init__(self, dry_run: bool = False):
        """Initialize the Reddit bot."""
        load_dotenv()
        self.dry_run = dry_run
        self.setup_logging()
        self.reddit = self.setup_reddit()
        self.commented_posts = self.load_commented_posts()
        self.stats = {
            'comments_posted': 0,
            'posts_skipped': 0,
            'errors': 0,
            'start_time': datetime.now()
        }
        
    def setup_logging(self):
        """Configure logging for the bot."""
        logging.basicConfig(
            level=getattr(logging, LOGGING['level']),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(LOGGING['file']),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger('RedditBot')
        
    def setup_reddit(self) -> praw.Reddit:
        """Setup Reddit API connection."""
        try:
            # Check if all required environment variables are present
            required_vars = {
                'REDDIT_CLIENT_ID': os.getenv('REDDIT_CLIENT_ID'),
                'REDDIT_CLIENT_SECRET': os.getenv('REDDIT_CLIENT_SECRET'),
                'REDDIT_USER_AGENT': os.getenv('REDDIT_USER_AGENT'),
                'REDDIT_USERNAME': os.getenv('REDDIT_USERNAME'),
                'REDDIT_PASSWORD': os.getenv('REDDIT_PASSWORD')
            }
            
            missing_vars = [var for var, value in required_vars.items() if not value or value.startswith('your_')]
            if missing_vars:
                self.logger.error(f"Missing or incomplete environment variables: {', '.join(missing_vars)}")
                self.logger.error("Please check your .env file and ensure all Reddit credentials are properly set.")
                sys.exit(1)
            
            self.logger.info("🔐 Attempting to connect to Reddit API...")
            
            reddit = praw.Reddit(
                client_id=required_vars['REDDIT_CLIENT_ID'],
                client_secret=required_vars['REDDIT_CLIENT_SECRET'],
                user_agent=required_vars['REDDIT_USER_AGENT'],
                username=required_vars['REDDIT_USERNAME'],
                password=required_vars['REDDIT_PASSWORD']
            )
            
            # Test the connection
            user = reddit.user.me()
            self.logger.info(f"✅ Successfully connected to Reddit as u/{user.name}")
            self.logger.info(f"📊 Account karma: {user.comment_karma + user.link_karma}")
            return reddit
            
        except Exception as e:
            self.logger.error(f"❌ Failed to connect to Reddit: {e}")
            
            # Provide specific troubleshooting advice based on error type
            error_str = str(e).lower()
            if "401" in error_str or "unauthorized" in error_str:
                self.logger.error("🔍 401 Unauthorized Error - This usually means:")
                self.logger.error("   1. Incorrect username or password")
                self.logger.error("   2. Wrong client ID or client secret")
                self.logger.error("   3. Reddit app is not configured as 'script' type")
                self.logger.error("   4. Account has 2FA enabled (not supported for script apps)")
                self.logger.error("📖 Check: https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps")
            elif "403" in error_str or "forbidden" in error_str:
                self.logger.error("🔍 403 Forbidden Error - This usually means:")
                self.logger.error("   1. Your Reddit app doesn't have the right permissions")
                self.logger.error("   2. Your user agent string is malformed")
                self.logger.error("   3. Rate limiting is in effect")
            else:
                self.logger.error("🔍 General troubleshooting:")
                self.logger.error("   1. Verify your .env file has correct Reddit credentials")
                self.logger.error("   2. Ensure your Reddit app is type 'script' not 'web app'")
                self.logger.error("   3. Check that your Reddit account can log in normally")
                
            sys.exit(1)
            
    def load_commented_posts(self) -> set:
        """Load the list of posts we've already commented on."""
        try:
            with open('commented_posts.json', 'r') as f:
                return set(json.load(f))
        except FileNotFoundError:
            return set()
        except Exception as e:
            self.logger.warning(f"Error loading commented posts: {e}")
            return set()
            
    def save_commented_posts(self):
        """Save the list of posts we've commented on."""
        try:
            with open('commented_posts.json', 'w') as f:
                json.dump(list(self.commented_posts), f)
        except Exception as e:
            self.logger.error(f"Error saving commented posts: {e}")
            
    def get_comment_text(self) -> str:
        """Get a random comment from templates or file."""
        try:
            if os.path.exists('comments.txt'):
                with open('comments.txt', 'r') as f:
                    comments = [line.strip() for line in f.readlines() if line.strip()]
                return random.choice(comments)
            else:
                return random.choice(COMMENT_TEMPLATES)
        except Exception as e:
            self.logger.error(f"Error getting comment text: {e}")
            return random.choice(COMMENT_TEMPLATES)
            
    def is_post_suitable(self, post) -> bool:
        """Check if a post is suitable for commenting."""
        try:
            # Skip our own posts
            if COMMENT_BEHAVIOR['avoid_own_posts'] and post.author == self.reddit.user.me():
                return False
                
            # Skip posts we've already commented on
            if COMMENT_BEHAVIOR['avoid_already_commented'] and post.id in self.commented_posts:
                return False
                
            # Check post age
            post_age = datetime.now() - datetime.fromtimestamp(post.created_utc)
            if post_age > timedelta(hours=POST_SELECTION['max_age_hours']):
                return False
                
            # Check post score
            if post.score < POST_SELECTION['min_score']:
                return False
                
            # Check number of comments
            if post.num_comments > POST_SELECTION['max_comments']:
                return False
                
            # Skip stickied posts
            if POST_SELECTION['skip_stickied'] and post.stickied:
                return False
                
            return True
            
        except Exception as e:
            self.logger.error(f"Error checking post suitability: {e}")
            return False
            
    def get_posts_from_subreddit(self, subreddit_name: str, limit: int = 25):
        """Get posts from a specific subreddit."""
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            if POST_SELECTION['sort_by'] == 'hot':
                posts = subreddit.hot(limit=limit)
            elif POST_SELECTION['sort_by'] == 'new':
                posts = subreddit.new(limit=limit)
            elif POST_SELECTION['sort_by'] == 'rising':
                posts = subreddit.rising(limit=limit)
            elif POST_SELECTION['sort_by'] == 'top':
                posts = subreddit.top(
                    time_filter=POST_SELECTION['time_filter'], 
                    limit=limit
                )
            else:
                posts = subreddit.hot(limit=limit)
                
            return [post for post in posts if self.is_post_suitable(post)]
            
        except Exception as e:
            self.logger.error(f"Error getting posts from r/{subreddit_name}: {e}")
            return []
            
    def post_comment(self, post, comment_text: str) -> bool:
        """Post a comment on a Reddit post."""
        try:
            if self.dry_run:
                self.logger.info(f"[DRY RUN] Would comment on '{post.title[:50]}...' in r/{post.subreddit}")
                self.logger.info(f"[DRY RUN] Comment: {comment_text}")
                return True
                
            # Post the comment
            comment = post.reply(comment_text)
            self.logger.info(f"✅ Posted comment on '{post.title[:50]}...' in r/{post.subreddit}")
            
            # Track this post
            self.commented_posts.add(post.id)
            self.stats['comments_posted'] += 1
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to comment on post: {e}")
            self.stats['errors'] += 1
            return False
            
    def wait_with_progress(self, delay: int):
        """Wait with a progress indicator."""
        self.logger.info(f"⏳ Waiting {delay} seconds before next action...")
        for i in range(delay):
            time.sleep(1)
            if i % 10 == 0 and i > 0:
                remaining = delay - i
                self.logger.debug(f"⏳ {remaining} seconds remaining...")
                
    def run_bot(self, max_comments: int = None):
        """Main bot execution function."""
        self.logger.info("🤖 Starting Reddit Bot...")
        
        if self.dry_run:
            self.logger.info("🧪 Running in DRY RUN mode - no comments will be posted")
            
        total_comments = 0
        max_total_comments = max_comments or len(TARGET_SUBREDDITS) * 5
        
        for subreddit_name in TARGET_SUBREDDITS:
            if total_comments >= max_total_comments:
                self.logger.info(f"🎯 Reached maximum comment limit ({max_total_comments})")
                break
                
            self.logger.info(f"🎯 Processing r/{subreddit_name}...")
            
            # Get posts from subreddit
            posts = self.get_posts_from_subreddit(subreddit_name)
            
            if not posts:
                self.logger.warning(f"⚠️  No suitable posts found in r/{subreddit_name}")
                self.stats['posts_skipped'] += 1
                continue
                
            # Comment on posts
            subreddit_comments = 0
            max_per_sub = int(os.getenv('MAX_COMMENTS_PER_SUBREDDIT', 5))
            
            for post in posts[:max_per_sub]:
                if total_comments >= max_total_comments:
                    break
                    
                comment_text = self.get_comment_text()
                
                if self.post_comment(post, comment_text):
                    total_comments += 1
                    subreddit_comments += 1
                    
                    # Random delay between comments
                    if total_comments < max_total_comments:
                        delay = random.randint(
                            RATE_LIMITS['min_delay'], 
                            RATE_LIMITS['max_delay']
                        )
                        self.wait_with_progress(delay)
                else:
                    self.stats['posts_skipped'] += 1
                    
            self.logger.info(f"📊 Posted {subreddit_comments} comments in r/{subreddit_name}")
            
            # Delay before switching subreddits
            if subreddit_name != TARGET_SUBREDDITS[-1] and total_comments < max_total_comments:
                self.wait_with_progress(RATE_LIMITS['subreddit_switch_delay'])
                
        # Save progress
        self.save_commented_posts()
        self.print_final_stats()
        
    def print_final_stats(self):
        """Print final execution statistics."""
        runtime = datetime.now() - self.stats['start_time']
        
        self.logger.info("📈 Final Statistics:")
        self.logger.info(f"   Comments Posted: {self.stats['comments_posted']}")
        self.logger.info(f"   Posts Skipped: {self.stats['posts_skipped']}")
        self.logger.info(f"   Errors: {self.stats['errors']}")
        self.logger.info(f"   Runtime: {runtime}")
        self.logger.info(f"   Subreddits Processed: {len(TARGET_SUBREDDITS)}")
        
    def interactive_mode(self):
        """Run the bot in interactive mode."""
        self.logger.info("🎮 Interactive Mode - Control the bot manually")
        
        while True:
            print("\n" + "="*50)
            print("Reddit Bot - Interactive Mode")
            print("="*50)
            print("1. Run bot with default settings")
            print("2. Run bot with custom comment limit")
            print("3. Test connection")
            print("4. View current stats")
            print("5. Preview next comment")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.run_bot()
            elif choice == '2':
                try:
                    limit = int(input("Enter maximum comments to post: "))
                    self.run_bot(max_comments=limit)
                except ValueError:
                    print("Invalid number entered.")
            elif choice == '3':
                try:
                    user = self.reddit.user.me()
                    print(f"✅ Connected as: {user}")
                    print(f"✅ Karma: {user.comment_karma + user.link_karma}")
                except Exception as e:
                    print(f"❌ Connection failed: {e}")
            elif choice == '4':
                self.print_final_stats()
            elif choice == '5':
                comment = self.get_comment_text()
                print(f"Next comment would be: '{comment}'")
            elif choice == '6':
                print("👋 Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    parser = argparse.ArgumentParser(description='Reddit Comment Bot')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Test the bot without posting comments')
    parser.add_argument('--interactive', action='store_true',
                       help='Run in interactive mode')
    parser.add_argument('--max-comments', type=int,
                       help='Maximum number of comments to post')
    
    args = parser.parse_args()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please copy .env.example to .env and fill in your Reddit credentials.")
        print("Get your credentials from: https://www.reddit.com/prefs/apps")
        sys.exit(1)
    
    # Create bot instance
    bot = RedditBot(dry_run=args.dry_run)
    
    try:
        if args.interactive:
            bot.interactive_mode()
        else:
            bot.run_bot(max_comments=args.max_comments)
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
        bot.save_commented_posts()
    except Exception as e:
        bot.logger.error(f"💥 Unexpected error: {e}")
        bot.save_commented_posts()

if __name__ == "__main__":
    main()
