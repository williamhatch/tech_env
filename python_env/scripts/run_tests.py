#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Automated script for running unit tests
"""

import os
import sys
import subprocess
import re

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

def colorize_test_output(line):
    """
    Colorize pytest output lines
    
    Args:
        line: A line of pytest output
    
    Returns:
        Colorized line
    """
    # Colorize test summary line
    if re.search(r'\d+ passed', line):
        line = re.sub(r'(\d+ passed)', f"{COLORS['GREEN']}\\1{COLORS['RESET']}", line)
    
    if re.search(r'\d+ failed', line):
        line = re.sub(r'(\d+ failed)', f"{COLORS['YELLOW']}\\1{COLORS['RESET']}", line)
        
    if re.search(r'\d+ error', line):
        line = re.sub(r'(\d+ error)', f"{COLORS['RED']}\\1{COLORS['RESET']}", line)
        
    if re.search(r'\d+ skipped', line):
        line = re.sub(r'(\d+ skipped)', f"{COLORS['BLUE']}\\1{COLORS['RESET']}", line)
    
    return line

def check_dependencies():
    """
    Check if required dependencies are installed
    
    Returns:
        dict: Dictionary with dependency status
    """
    dependencies = {
        'pytest-cov': False,
        'fastapi': False,
    }
    
    # Check pytest-cov
    try:
        import pytest_cov
        dependencies['pytest-cov'] = True
    except ImportError:
        pass
    
    # Check fastapi
    try:
        import fastapi
        dependencies['fastapi'] = True
    except ImportError:
        pass
        
    return dependencies

def run_tests(coverage=True):
    """
    Run tests and optionally generate coverage report
    
    Args:
        coverage: Whether to generate coverage report
    """
    print(colorize("\n" + "="*50, 'CYAN'))
    print(colorize("RUNNING TESTS".center(50), 'CYAN'))
    print(colorize("="*50 + "\n", 'CYAN'))
    
    print(colorize("Running tests...", 'GREEN'))
    
    cmd = ["pytest", "-v"]
    
    # Check dependencies
    deps = check_dependencies()
    missing_deps = [dep for dep, installed in deps.items() if not installed]
    
    # Only add coverage options if pytest-cov is installed
    if coverage and deps['pytest-cov']:
        cmd.extend(["--cov=src", "--cov-report", "term", "--cov-report", "html"])
    elif coverage:
        print(colorize("\nWarning: pytest-cov is not installed. Running tests without coverage.", 'YELLOW'))
        print(colorize("To install pytest-cov, run: pip install pytest-cov\n", 'YELLOW'))
    
    # Show warnings for missing dependencies
    if missing_deps:
        print(colorize("\nWarning: Some dependencies are missing:", 'YELLOW'))
        for dep in missing_deps:
            print(colorize(f"  - {dep}", 'YELLOW'))
        print(colorize("\nTo install all dependencies, run: pip install -r requirements.txt\n", 'YELLOW'))
    
    # Use Popen to capture and colorize output in real-time
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )
    
    # Process and colorize output
    for line in process.stdout:
        sys.stdout.write(colorize_test_output(line))
    
    process.wait()
    
    # Show coverage report location if enabled
    if coverage and process.returncode == 0:
        print(colorize("\n" + "="*50, 'CYAN'))
        print(colorize("COVERAGE REPORT".center(50), 'CYAN'))
        print(colorize("="*50, 'CYAN'))
        
        coverage_dir = os.path.join(os.getcwd(), 'htmlcov')
        if os.path.exists(coverage_dir):
            index_file = os.path.join(coverage_dir, 'index.html')
            if os.path.exists(index_file):
                print(colorize("\nCoverage report generated at: ", 'BLUE') + 
                      colorize("htmlcov/index.html", 'GREEN'))
                print(colorize("Open with: ", 'BLUE') + 
                      colorize("open htmlcov/index.html", 'GREEN') + "\n")
            else:
                print(colorize("\nCoverage directory exists but no index.html found.", 'YELLOW'))
        else:
            print(colorize("\nNo coverage directory found. Make sure pytest-cov is configured correctly.", 'YELLOW'))
    
    return process.returncode


if __name__ == "__main__":
    # Change to project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Parse command line arguments
    coverage = True
    if len(sys.argv) > 1 and sys.argv[1] == "--no-coverage":
        coverage = False
        print(colorize("Running tests without coverage report", 'BLUE'))
    else:
        print(colorize("Running tests with coverage report", 'BLUE'))
    
    # Run tests
    exit_code = run_tests(coverage)
    sys.exit(exit_code)
