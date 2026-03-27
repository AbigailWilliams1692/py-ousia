# Contributing to py-ousia

Thank you for your interest in contributing to py-ousia! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git

### Setting Up the Development Environment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd py-ousia
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix/macOS
   source .venv/bin/activate
   ```

3. Install the package in development mode:
   ```bash
   python -m pip install -e .
   ```

## Development Workflow

### Code Style

This project follows standard Python code style conventions:
- Use `black` for code formatting
- Use `flake8` for linting

Run the formatting and linting tools:
```bash
python -m black ousia/
python -m flake8 ousia/
```

### Testing

Run tests with:
```bash
python -m pytest
```

### Submitting Changes

1. Create a new branch for your feature or bugfix
2. Make your changes following the code style guidelines
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request with a clear description of your changes

## Project Structure

```
py-ousia/
├── ousia/
│   ├── base_model/          # Core entity-attribute framework
│   │   ├── __init__.py
│   │   ├── entity.py
│   │   └── attribute.py
│   └── finance_model/       # Financial entity model extensions
│       └── __init__.py
├── tests/                   # Test files
├── project.json            # Project configuration
├── README.md
└── CONTRIBUTING.md
```

## Guidelines

- Keep code simple and readable
- Add docstrings for all public methods and classes
- Follow the existing code patterns and conventions
- Write tests for new functionality
- Update documentation as needed

## Questions

If you have questions about contributing, feel free to open an issue for discussion.
