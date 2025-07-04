# Contributing to Reddit Comment Bot

Thank you for considering contributing to the Reddit Comment Bot! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Issues

1. **Check existing issues** first to avoid duplicates
2. **Use the issue templates** when available
3. **Provide detailed information**:
   - OS and Python version
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages or logs
   - Screenshots if applicable

### Suggesting Features

1. **Open a discussion** first for major features
2. **Explain the use case** and why it's needed
3. **Consider the impact** on existing functionality
4. **Propose implementation** if you have ideas

### Code Contributions

#### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/Reddit-Comment-Bot.git
   cd Reddit-Comment-Bot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

4. **Create your feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

#### Code Standards

- **Python 3.7+** compatibility required
- **PEP 8** style guide compliance
- **Type hints** encouraged for new code
- **Docstrings** for all public functions and classes
- **Comments** for complex logic

#### Testing

1. **Test your changes** thoroughly
2. **Run existing tests** to ensure nothing breaks
3. **Add tests** for new functionality
4. **Test with different configurations**

```bash
# Test imports
python -c "import reddit_bot; import config; import utils"

# Test credential checker
python test_credentials.py

# Test dry run
python reddit_bot.py --dry-run --max-comments 1
```

#### Commit Guidelines

- **Use clear, descriptive commit messages**
- **Follow conventional commits** format when possible:
  ```
  feat: add new comment filtering option
  fix: resolve rate limiting issue
  docs: update setup instructions
  style: format code with black
  refactor: reorganize utility functions
  test: add unit tests for post filtering
  ```

- **Keep commits focused** - one feature/fix per commit
- **Include issue numbers** when applicable: `fixes #123`

#### Pull Request Process

1. **Update documentation** for any new features
2. **Add/update tests** as needed
3. **Ensure CI passes** before requesting review
4. **Fill out the PR template** completely
5. **Request review** from maintainers

### Documentation Contributions

- **README improvements** are always welcome
- **Add examples** for new features
- **Fix typos** and improve clarity
- **Translate documentation** to other languages

## 🛡️ Safety and Ethics

### Responsible Development

All contributions must:

- ✅ **Promote responsible usage** of Reddit's API
- ✅ **Include appropriate warnings** about misuse
- ✅ **Respect rate limits** and platform guidelines
- ✅ **Encourage quality content** over spam
- ❌ **NOT enable malicious behavior**

### Code Review Focus Areas

- **Security**: Credential handling, input validation
- **Safety**: Rate limiting, error handling
- **Ethics**: Encouraging responsible usage
- **Performance**: Efficient API usage
- **Maintainability**: Clean, readable code

## 📋 Development Guidelines

### Project Structure

```
Reddit-Comment-Bot/
├── reddit_bot.py          # Main bot logic
├── config.py              # Configuration settings
├── utils.py               # Utility functions
├── test_credentials.py    # Credential testing
├── comments.txt           # Comment templates
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
└── docs/                 # Documentation
```

### Adding New Features

1. **Consider backwards compatibility**
2. **Update configuration options** in `config.py`
3. **Add appropriate logging** statements
4. **Include error handling**
5. **Update documentation**

### Code Style

```python
# Good: Clear, documented function
def filter_posts_by_age(posts: List[Post], max_age_hours: int = 24) -> List[Post]:
    """
    Filter posts by age to avoid commenting on old content.
    
    Args:
        posts: List of Reddit posts to filter
        max_age_hours: Maximum age in hours for posts to include
        
    Returns:
        List of posts within the age limit
    """
    cutoff_time = datetime.now() - timedelta(hours=max_age_hours)
    return [post for post in posts if post.created_utc > cutoff_time.timestamp()]
```

### Error Handling

```python
# Good: Comprehensive error handling
try:
    reddit = praw.Reddit(**credentials)
    user = reddit.user.me()
    logger.info(f"Connected as: {user.name}")
except praw.exceptions.InvalidUserPass:
    logger.error("Invalid username or password")
    return False
except praw.exceptions.ResponseException as e:
    logger.error(f"Reddit API error: {e}")
    return False
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return False
```

## 🚀 Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes

### Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Test on multiple Python versions
- [ ] Update documentation
- [ ] Create release notes
- [ ] Tag the release

## 📞 Getting Help

- **GitHub Discussions** for questions and ideas
- **GitHub Issues** for bugs and feature requests
- **Code Review** for implementation feedback

## 🎯 Priority Areas

We're particularly interested in contributions for:

1. **Enhanced safety features**
2. **Better error handling and recovery**
3. **Improved documentation**
4. **Additional configuration options**
5. **Performance optimizations**
6. **Multi-language support**

## 📜 Code of Conduct

### Our Standards

- **Be respectful** and inclusive
- **Focus on constructive feedback**
- **Help others learn and grow**
- **Promote responsible bot usage**

### Unacceptable Behavior

- Harassment or discrimination
- Promoting malicious bot usage
- Sharing credentials or personal information
- Spam or off-topic discussions

## 🙏 Recognition

Contributors will be:
- **Listed in CONTRIBUTORS.md**
- **Mentioned in release notes**
- **Credited in documentation**

Thank you for helping make Reddit Comment Bot better! 🤖✨
