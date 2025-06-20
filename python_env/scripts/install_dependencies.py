#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to install all required dependencies
"""

import os
import sys
import subprocess

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

def install_dependencies():
    """
    Install all required dependencies from requirements.txt
    """
    print(colorize("\n" + "="*50, 'CYAN'))
    print(colorize("INSTALLING DEPENDENCIES".center(50), 'CYAN'))
    print(colorize("="*50 + "\n", 'CYAN'))
    
    # Change to project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print(colorize("Error: requirements.txt not found!", 'RED'))
        return False
    
    print(colorize("Installing dependencies from requirements.txt...", 'GREEN'))
    
    # Install dependencies
    cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    process = subprocess.run(cmd, capture_output=True, text=True)
    
    if process.returncode == 0:
        print(colorize("\nDependencies installed successfully!", 'GREEN'))
        
        # List installed packages
        print(colorize("\nInstalled packages:", 'BLUE'))
        subprocess.run([sys.executable, "-m", "pip", "list"])
        
        return True
    else:
        print(colorize("\nError installing dependencies:", 'RED'))
        print(colorize(process.stderr, 'RED'))
        return False

if __name__ == "__main__":
    success = install_dependencies()
    if success:
        print(colorize("\nYou can now run tests with:", 'BLUE'))
        print(colorize("  python scripts/run_tests.py", 'GREEN'))
        print(colorize("\nOr watch for file changes with:", 'BLUE'))
        print(colorize("  python scripts/watch_tests.py", 'GREEN'))
    else:
        sys.exit(1)
