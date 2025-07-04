#!/usr/bin/env python3
"""
Reddit Bot Utilities
Helper script for managing the Reddit bot.
"""

import json
import os
import sys
from datetime import datetime
import argparse

def view_stats():
    """View bot statistics."""
    print("📊 Reddit Bot Statistics")
    print("=" * 40)
    
    # Check if log file exists
    if os.path.exists('bot.log'):
        with open('bot.log', 'r') as f:
            lines = f.readlines()
            print(f"📝 Log entries: {len(lines)}")
            
            # Count different types of messages
            info_count = sum(1 for line in lines if 'INFO' in line)
            error_count = sum(1 for line in lines if 'ERROR' in line)
            warning_count = sum(1 for line in lines if 'WARNING' in line)
            
            print(f"ℹ️  Info messages: {info_count}")
            print(f"⚠️  Warnings: {warning_count}")
            print(f"❌ Errors: {error_count}")
    else:
        print("📝 No log file found")
    
    # Check commented posts
    if os.path.exists('commented_posts.json'):
        with open('commented_posts.json', 'r') as f:
            posts = json.load(f)
            print(f"💬 Posts commented on: {len(posts)}")
    else:
        print("💬 No commented posts recorded")
    
    print()

def clear_history():
    """Clear bot history."""
    confirm = input("⚠️  Are you sure you want to clear all bot history? (yes/no): ")
    if confirm.lower() == 'yes':
        files_to_remove = ['commented_posts.json', 'bot.log']
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)
                print(f"🗑️  Removed {file}")
        print("✅ History cleared")
    else:
        print("❌ Operation cancelled")

def backup_data():
    """Backup bot data."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backup_{timestamp}"
    
    os.makedirs(backup_dir, exist_ok=True)
    
    files_to_backup = ['commented_posts.json', 'bot.log', '.env', 'config.py']
    backed_up = 0
    
    for file in files_to_backup:
        if os.path.exists(file):
            import shutil
            shutil.copy2(file, backup_dir)
            backed_up += 1
    
    print(f"💾 Backed up {backed_up} files to {backup_dir}/")

def test_config():
    """Test bot configuration."""
    print("🔧 Testing Configuration")
    print("=" * 30)
    
    # Test .env file
    if os.path.exists('.env'):
        print("✅ .env file found")
        from dotenv import load_dotenv
        load_dotenv()
        
        required_vars = [
            'REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET', 
            'REDDIT_USER_AGENT', 'REDDIT_USERNAME', 'REDDIT_PASSWORD'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not os.getenv(var) or os.getenv(var) == f'your_{var.lower()}_here':
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Missing or incomplete variables: {', '.join(missing_vars)}")
        else:
            print("✅ All required environment variables found")
    else:
        print("❌ .env file not found")
    
    # Test config.py
    try:
        from config import TARGET_SUBREDDITS, COMMENT_TEMPLATES
        print(f"✅ Configuration loaded - {len(TARGET_SUBREDDITS)} subreddits, {len(COMMENT_TEMPLATES)} comment templates")
    except Exception as e:
        print(f"❌ Error loading config.py: {e}")
    
    # Test comments file
    if os.path.exists('comments.txt'):
        with open('comments.txt', 'r') as f:
            comments = [line.strip() for line in f.readlines() if line.strip()]
            print(f"✅ Comments file loaded - {len(comments)} comments available")
    else:
        print("⚠️  comments.txt not found, will use default templates")

def show_last_activity():
    """Show last bot activity."""
    if not os.path.exists('bot.log'):
        print("📝 No activity log found")
        return
    
    print("📅 Recent Bot Activity")
    print("=" * 30)
    
    with open('bot.log', 'r') as f:
        lines = f.readlines()
        
    # Show last 10 lines
    recent_lines = lines[-10:]
    for line in recent_lines:
        print(line.strip())

def main():
    parser = argparse.ArgumentParser(description='Reddit Bot Utilities')
    parser.add_argument('--stats', action='store_true', help='View bot statistics')
    parser.add_argument('--clear', action='store_true', help='Clear bot history')
    parser.add_argument('--backup', action='store_true', help='Backup bot data')
    parser.add_argument('--test', action='store_true', help='Test configuration')
    parser.add_argument('--activity', action='store_true', help='Show recent activity')
    
    args = parser.parse_args()
    
    if args.stats:
        view_stats()
    elif args.clear:
        clear_history()
    elif args.backup:
        backup_data()
    elif args.test:
        test_config()
    elif args.activity:
        show_last_activity()
    else:
        # Interactive menu
        while True:
            print("\n🤖 Reddit Bot Utilities")
            print("=" * 30)
            print("1. View Statistics")
            print("2. Test Configuration")
            print("3. Show Recent Activity")
            print("4. Backup Data")
            print("5. Clear History")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                view_stats()
            elif choice == '2':
                test_config()
            elif choice == '3':
                show_last_activity()
            elif choice == '4':
                backup_data()
            elif choice == '5':
                clear_history()
            elif choice == '6':
                print("👋 Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
