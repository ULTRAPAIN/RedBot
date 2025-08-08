# Reddit Comment Bot - GitHub Copilot Instructions

**ALWAYS follow these instructions first.** Only fallback to additional search and context gathering if the information here is incomplete or found to be in error.

## Working Effectively

### Quick Setup and Validation
```bash
# Install dependencies (takes ~7 seconds)
pip install -r requirements.txt

# Test imports (takes ~1 second each)
python3 -c "import reddit_bot; print('✅ reddit_bot module imports successfully')"
python3 -c "import config; print('✅ config module imports successfully')"
python3 -c "import utils; print('✅ utils module imports successfully')"

# Setup environment file
cp .env.example .env
# Edit .env with actual Reddit API credentials

# Test credentials without posting
python3 test_credentials.py

# Test bot in safe mode
python3 reddit_bot.py --dry-run --max-comments 1
```

### Build and Test Process
**NEVER CANCEL**: All commands complete quickly (< 30 seconds). Set timeout to 60+ seconds for safety.

```bash
# Install all testing dependencies (takes ~30 seconds)
pip install flake8 pytest bandit safety

# Critical linting (MUST pass - takes ~1 second)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Style linting (warnings OK - takes ~1 second) 
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics

# Security scan (low-severity warnings expected - takes ~1 second)
bandit -r . -x ./test_*

# Safety check (takes ~5 seconds)
safety check
```

### Running the Application
```bash
# ALWAYS test credentials first
python3 test_credentials.py

# Safe testing modes
python3 reddit_bot.py --dry-run                    # No actual posts
python3 reddit_bot.py --interactive                # Manual approval
python3 reddit_bot.py --dry-run --max-comments 3   # Limited test

# Live operation (start conservatively!)
python3 reddit_bot.py --max-comments 5             # Limited run
python3 reddit_bot.py                              # Full operation
```

## Validation Requirements

### CRITICAL: After ANY code changes, ALWAYS run:
1. **Import test**: `python3 -c "import reddit_bot; import config; import utils"`
2. **Credential test**: `python3 test_credentials.py` (should show credential status)
3. **Dry run test**: `python3 reddit_bot.py --dry-run --max-comments 1`
4. **Linting**: `flake8 . --select=E9,F63,F7,F82` (MUST pass)
5. **Stats test**: `python3 utils.py --stats` (should display statistics)

### Manual Testing Scenarios
**MANDATORY**: Test these complete user workflows after making changes:

#### Scenario 1: Fresh Setup
```bash
# Simulate new user setup
rm -f .env bot.log
python3 test_credentials.py    # Should prompt for interactive setup
cp .env.example .env           # User creates credentials
python3 test_credentials.py    # Should show missing credentials
# User edits .env with real credentials
python3 test_credentials.py    # Should connect successfully
python3 reddit_bot.py --dry-run --max-comments 1  # Should work without posting
```

#### Scenario 2: Configuration Testing
```bash
# Test configuration validation
python3 -c "from config import TARGET_SUBREDDITS, COMMENT_TEMPLATES; print(f'Subreddits: {len(TARGET_SUBREDDITS)}, Comments: {len(COMMENT_TEMPLATES)}')"

# Test comment loading
python3 -c "
import reddit_bot
bot = reddit_bot.RedditBot(dry_run=True)
comment = bot.get_comment_text()
print(f'Generated comment: {comment[:50]}...')
"
```

#### Scenario 3: Error Handling
```bash
# Test with missing credentials
mv .env .env.backup
python3 reddit_bot.py --dry-run  # Should fail gracefully with clear error

# Test with invalid credentials  
echo "REDDIT_CLIENT_ID=invalid" > .env
python3 test_credentials.py      # Should show authentication failure

# Restore valid config
mv .env.backup .env
```

## Project Structure and Key Files

### Core Application Files
- **`reddit_bot.py`**: Main bot logic and Reddit API interaction
- **`config.py`**: Configuration settings (subreddits, comments, rate limits)
- **`utils.py`**: Management tools (stats, monitoring, backup)
- **`test_credentials.py`**: Credential validation and setup helper
- **`comments.txt`**: Template comments for bot to use

### Configuration Files
- **`.env`**: Reddit API credentials (NEVER commit this file)
- **`.env.example`**: Template for environment setup
- **`requirements.txt`**: Python dependencies
- **`.gitignore`**: Includes .env to prevent credential leaks

### Setup and Automation
- **`setup.sh`**: Automated installation script
- **`github_setup.sh`**: Repository initialization script
- **`.github/workflows/ci.yml`**: CI/CD pipeline

## Build System Details

### Dependencies
**Required Python version**: 3.7+
**Key packages**:
- `praw==7.8.1` (Python Reddit API Wrapper)
- `python-dotenv==1.0.0` (Environment variable loading)
- `requests==2.31.0` (HTTP requests)

### Installation Commands
```bash
# Basic setup (NEVER CANCEL - takes ~7 seconds)
pip install -r requirements.txt

# Development tools (takes ~30 seconds)
pip install flake8 pytest bandit safety

# Automated setup option
chmod +x setup.sh && ./setup.sh
```

### Environment Setup
**Critical**: The `.env` file contains sensitive Reddit API credentials:
```bash
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here  
REDDIT_USER_AGENT=RedditBot/1.0 by YourUsername
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
```

## Configuration Management

### Key Configuration Areas
**`config.py`** contains these important settings:
- **TARGET_SUBREDDITS**: List of subreddits to target
- **COMMENT_TEMPLATES**: Default comment options
- **POST_SELECTION**: Criteria for selecting posts (age, score, etc.)
- **RATE_LIMITS**: Timing between comments (critical for avoiding rate limits)
- **COMMENT_BEHAVIOR**: Safety settings and retry logic

### Common Configuration Tasks
```bash
# Check current configuration
python3 -c "
from config import TARGET_SUBREDDITS, RATE_LIMITS
print(f'Targeting {len(TARGET_SUBREDDITS)} subreddits')
print(f'Rate limits: {RATE_LIMITS[\"min_delay\"]}-{RATE_LIMITS[\"max_delay\"]} seconds')
"

# Validate comment templates
python3 -c "
from config import COMMENT_TEMPLATES
print(f'Loaded {len(COMMENT_TEMPLATES)} comment templates')
print(f'Sample: {COMMENT_TEMPLATES[0][:50]}...')
"
```

## Timing Expectations

### Command Execution Times
- **Dependency installation**: ~7 seconds (NEVER CANCEL)
- **Module imports**: ~1 second each
- **Credential testing**: ~2-5 seconds  
- **Linting (critical)**: ~1 second
- **Linting (full)**: ~1 second
- **Security scanning**: ~1 second
- **Dry run testing**: ~3-10 seconds
- **Stats generation**: ~1 second

**TIMEOUT RECOMMENDATIONS**: Set all timeouts to 60+ seconds minimum for safety.

## CI/CD Pipeline Details

### GitHub Actions Workflow
**Location**: `.github/workflows/ci.yml`
**Tests multiple Python versions**: 3.7, 3.8, 3.9, 3.10, 3.11

**Pipeline steps**:
1. Install dependencies
2. Critical syntax linting (MUST pass)
3. Style linting (warnings OK)
4. Import testing
5. Security scanning
6. Basic functionality tests

### Pre-commit Validation
**ALWAYS run before committing**:
```bash
# Critical checks (MUST pass)
flake8 . --select=E9,F63,F7,F82 --show-source --statistics

# Import validation
python3 -c "import reddit_bot; import config; import utils"

# Functional test
python3 reddit_bot.py --dry-run --max-comments 1
```

## Safety and Security Features

### Built-in Protections
- **Rate limiting**: 30-120 second delays between comments
- **Post filtering**: Age limits, score thresholds, comment count limits
- **Duplicate prevention**: Tracks previously commented posts
- **Dry run mode**: Test without posting actual comments
- **Interactive mode**: Manual approval for each action

### Security Considerations
- **Credential management**: Uses .env file, never hardcoded
- **API rate limiting**: Respects Reddit's API limits
- **Error handling**: Graceful failure modes
- **Logging**: Comprehensive activity tracking

### Expected Security Scan Results
Bandit will report **low-severity warnings** about pseudo-random generators - this is expected and acceptable for this application type.

## Troubleshooting Common Issues

### Import Errors
```bash
# Test each module individually
python3 -c "import reddit_bot"  # Main bot functionality
python3 -c "import config"      # Configuration system  
python3 -c "import utils"       # Utility functions
python3 -c "import praw"        # Reddit API wrapper
```

### Credential Issues
```bash
# Check .env file exists and has content
ls -la .env
head .env

# Test credential validation
python3 test_credentials.py

# Common fixes:
cp .env.example .env    # Create from template
# Edit .env with actual Reddit API credentials
```

### Rate Limiting Errors
- Increase delays in `config.py` RATE_LIMITS section
- Reduce MAX_COMMENTS_PER_SUBREDDIT
- Wait longer between bot runs

### Permission Errors
- Check subreddit rules (some restrict new accounts)
- Verify Reddit account has sufficient karma
- Check for subreddit-specific posting restrictions

## Development Best Practices

### Code Style
- Follow PEP 8 guidelines
- Line length limit: 100 characters
- Use meaningful variable names
- Add docstrings for functions

### Making Changes
1. **Always test imports** after code changes
2. **Run dry-run mode** to validate functionality
3. **Check linting** before committing
4. **Update configuration** if adding new features
5. **Test error scenarios** to ensure graceful handling

### Adding New Features
- Update `config.py` for new configuration options
- Add appropriate logging statements  
- Include error handling for new code paths
- Test in dry-run mode extensively
- Update documentation if needed

## Frequently Used Commands Reference

```bash
# Quick validation suite
python3 -c "import reddit_bot; import config; import utils" && \
python3 test_credentials.py --quick && \
python3 reddit_bot.py --dry-run --max-comments 1 && \
flake8 . --select=E9,F63,F7,F82

# Development testing
python3 reddit_bot.py --dry-run --interactive
python3 utils.py --stats
python3 utils.py --activity

# Clean testing environment
rm -f bot.log .env && cp .env.example .env

# CI pipeline simulation
pip install flake8 bandit safety && \
flake8 . --select=E9,F63,F7,F82 --show-source --statistics && \
bandit -r . -x ./test_* && \
safety check
```

Remember: This bot interacts with Reddit's API and must be used responsibly in accordance with Reddit's Terms of Service and individual subreddit rules.