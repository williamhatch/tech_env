#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script for watching file changes and automatically running tests
"""

import os
import sys
import time
import subprocess
from pathlib import Path

# ANSI color codes
COLORS = {
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'RED': '\033[31m',
    'BLUE': '\033[34m',
    'CYAN': '\033[36m',
    'MAGENTA': '\033[35m',
    'RESET': '\033[0m'
}

def colorize(text, color):
    """
    Add color to the given text
    
    Args:
        text: Text to colorize
        color: Color to use from COLORS dict
    
    Returns:
        Colorized text string
    """
    return f"{COLORS[color]}{text}{COLORS['RESET']}"

def run_pytest_watch():
    """
    Use pytest-watch to monitor file changes and automatically run tests
    """
    print(colorize("\n" + "="*50, 'CYAN'))
    print(colorize("TEST WATCHER".center(50), 'CYAN'))
    print(colorize("="*50 + "\n", 'CYAN'))
    
    print(colorize("Starting test watcher...", 'GREEN'))
    print(colorize("Watching for file changes in src and tests directories...", 'BLUE'))
    print(colorize("Press Ctrl+C to exit", 'YELLOW'))
    
    # Display coverage report info
    print(colorize("\n" + "="*50, 'CYAN'))
    print(colorize("COVERAGE REPORT INFO".center(50), 'CYAN'))
    print(colorize("="*50, 'CYAN'))
    print(colorize("\nCoverage report will be generated at: ", 'BLUE') + 
          colorize("htmlcov/index.html", 'GREEN'))
    print(colorize("After tests run, open with: ", 'BLUE') + 
          colorize("open htmlcov/index.html", 'GREEN') + "\n")
    
    # Use pytest directly with watch mode
    print(colorize("\nRunning tests with pytest and watching for changes...", 'GREEN'))
    
    # Use python -m pytest_watch to ensure we're using the installed module
    cmd = ["python", "-m", "pytest_watch", "--clear", "--runner", "pytest -v --cov=src --cov-report term --cov-report html", "src", "tests"]
    subprocess.run(cmd)


def check_directories():
    """
    Check if necessary directories exist, create them if they don't
    """
    project_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    src_dir = project_root / "src"
    tests_dir = project_root / "tests"
    
    # Ensure src directory exists
    if not src_dir.exists():
        print(colorize(f"Creating source code directory: {src_dir}", 'MAGENTA'))
        src_dir.mkdir(parents=True, exist_ok=True)
        
        # Create __init__.py file to make it a package
        init_file = src_dir / "__init__.py"
        if not init_file.exists():
            init_file.touch()
            print(colorize(f"Created {init_file}", 'BLUE'))
    
    # Ensure tests directory exists
    if not tests_dir.exists():
        print(colorize(f"Creating test directory: {tests_dir}", 'MAGENTA'))
        tests_dir.mkdir(parents=True, exist_ok=True)
        
        # Create __init__.py file to make it a package
        init_file = tests_dir / "__init__.py"
        if not init_file.exists():
            init_file.touch()
            print(colorize(f"Created {init_file}", 'BLUE'))


if __name__ == "__main__":
    # Change to project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Check and create necessary directories
    check_directories()
    
    # Run test watcher
    run_pytest_watch()
