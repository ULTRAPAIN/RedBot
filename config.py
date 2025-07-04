# Bot Configuration
# Edit this file to customize your bot's behavior

# Target Subreddits (without 'r/' prefix)
TARGET_SUBREDDITS = [
    'AskReddit',
    'funny',
    'pics',
    'videos',
    'todayilearned',
    'worldnews',
    'science',
    'technology',
    'gaming',
    'movies'
]

# Comment Templates
# The bot will randomly choose from these comments
COMMENT_TEMPLATES = [
    "Great post! Thanks for sharing.",
    "This is really interesting!",
    "I completely agree with this.",
    "Thanks for the insight!",
    "This made my day better.",
    "Awesome content!",
    "Well said!",
    "I learned something new today.",
    "This is exactly what I needed to see.",
    "Brilliant perspective!"
]

# Post Selection Criteria
POST_SELECTION = {
    'sort_by': 'hot',  # Options: hot, new, rising, top
    'time_filter': 'day',  # For 'top' sort: hour, day, week, month, year, all
    'min_score': 10,  # Minimum upvotes for a post to be considered
    'max_age_hours': 24,  # Maximum age of posts to comment on (in hours)
    'max_comments': 500,  # Don't comment on posts with too many comments
    'skip_stickied': True,  # Skip pinned/stickied posts
}

# Comment Behavior
COMMENT_BEHAVIOR = {
    'max_retries': 3,  # Maximum retry attempts for failed comments
    'avoid_own_posts': True,  # Don't comment on your own posts
    'avoid_already_commented': True,  # Don't comment on posts you've already commented on
    'min_comment_length': 10,  # Minimum length for comments
}

# Rate Limiting (in seconds)
RATE_LIMITS = {
    'min_delay': 30,  # Minimum delay between comments
    'max_delay': 120,  # Maximum delay between comments
    'subreddit_switch_delay': 60,  # Delay when switching to a new subreddit
}

# Logging Configuration
LOGGING = {
    'level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    'file': 'bot.log',
    'max_size_mb': 10,  # Maximum log file size in MB
}
