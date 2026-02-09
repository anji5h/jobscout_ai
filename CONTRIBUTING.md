# Contributing to JobScout AI

Thank you for considering contributing to JobScout AI! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## 📜 Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/jobscout_ai.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Set up your development environment (see README.md)

## 🤝 How to Contribute

### Reporting Bugs

- Use the GitHub Issues page
- Check if the bug has already been reported
- Use the bug report template
- Include:
  - Clear description
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots (if applicable)
  - Environment details

### Suggesting Features

- Use the GitHub Issues page
- Use the feature request template
- Describe the feature and its benefits
- Explain use cases

### Code Contributions

1. **Find an issue to work on** or create one
2. **Comment on the issue** to let others know you're working on it
3. **Fork and branch** from `main`
4. **Write code** following our standards
5. **Test your changes** thoroughly
6. **Update documentation** if needed
7. **Submit a pull request**

## 💻 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Maximum line length: 88 characters (Black formatter)
- Use type hints where applicable

```python
# Good example
def calculate_match_score(job_requirements: list[str], user_skills: list[str]) -> float:
    """
    Calculate the match score between job requirements and user skills.
    
    Args:
        job_requirements: List of required skills for the job
        user_skills: List of skills the user possesses
    
    Returns:
        A float between 0 and 1 representing the match score
    """
    # Implementation here
    pass
```

### Code Comments

- Write self-documenting code when possible
- Add comments for complex logic
- Use docstrings for all functions, classes, and modules
- Keep comments up-to-date with code changes

```python
# Good: Explains WHY, not WHAT
# Calculate weighted score to prioritize exact matches over partial matches
score = exact_matches * 2 + partial_matches

# Avoid: States the obvious
# Add two numbers together
result = a + b
```

### Directory Structure

```
src/
├── models/          # Data models
├── services/        # Business logic
├── utils/           # Helper functions
├── api/             # API endpoints
└── tests/           # Unit and integration tests
```

## 📝 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(search): add AI-powered job matching algorithm

fix(auth): resolve session timeout issue

docs(readme): update installation instructions
```

## 🔄 Pull Request Process

1. **Update your branch** with the latest main branch
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-feature-branch
   git rebase main
   ```

2. **Ensure all tests pass**
   ```bash
   pytest tests/
   ```

3. **Update documentation** if you've changed functionality

4. **Create a pull request** with:
   - Clear title and description
   - Reference to related issues
   - Screenshots (if UI changes)
   - Test results

5. **Wait for review** - maintainers will review your PR
   - Address any feedback
   - Keep the conversation professional and constructive

6. **Merge** - Once approved, your PR will be merged!

## ✅ Checklist Before Submitting PR

- [ ] Code follows project style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated and passing
- [ ] No new warnings generated
- [ ] Commit messages follow guidelines
- [ ] PR description is clear and complete

## 🆘 Need Help?

- Check existing issues and documentation
- Ask questions in issue comments
- Reach out to maintainers

Thank you for contributing! 🙌
