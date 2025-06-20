#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to run the FastAPI application
"""

import os
import sys
import uvicorn
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


def run_api(host="127.0.0.1", port=8000, reload=True):
    """
    Run the FastAPI application
    
    Args:
        host: Host to bind the server to
        port: Port to bind the server to
        reload: Whether to reload the server on code changes
    """
    print(colorize("\n" + "="*50, 'CYAN'))
    print(colorize("STARTING API SERVER".center(50), 'CYAN'))
    print(colorize("="*50 + "\n", 'CYAN'))
    
    # Change to project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Ensure src directory is in path
    sys.path.insert(0, os.getcwd())
    
    print(colorize(f"Starting FastAPI server at http://{host}:{port}", 'GREEN'))
    print(colorize("API documentation will be available at:", 'BLUE'))
    print(colorize(f"http://{host}:{port}/docs", 'BLUE'))
    print(colorize(f"http://{host}:{port}/redoc", 'BLUE'))
    
    # Run the server
    uvicorn.run(
        "src.app:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


if __name__ == "__main__":
    run_api()
