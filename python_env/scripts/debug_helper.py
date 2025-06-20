#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Debug helper for Python environment
Provides various debugging tools and helper functions to assist with rapid code debugging
"""

import sys
import os
import inspect

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
    """Add color to text"""
    return f"{COLORS[color]}{text}{COLORS['RESET']}"

def debug_break():
    """
    Insert a breakpoint in the code
    Usage:
    from scripts.debug_helper import debug_break
    
    def some_function():
        x = 10
        y = 20
        debug_break()  # Code execution will pause here
        z = x + y
    """
    try:
        import ipdb
        ipdb.set_trace(context=5)  # Show 5 lines of code around the breakpoint
    except ImportError:
        try:
            import pdb
            pdb.set_trace()
        except ImportError:
            print(colorize("Unable to import debugger module. Please install ipdb: pip install ipdb", 'RED'))

def trace_function(func):
    """
    Function decorator to trace variable changes during function execution
    Usage:
    from scripts.debug_helper import trace_function
    
    @trace_function
    def calculate_sum(a, b):
        result = a + b
        return result
    """
    try:
        import pysnooper
        return pysnooper.snoop()(func)
    except ImportError:
        print(colorize("Unable to import pysnooper module. Please install: pip install pysnooper", 'YELLOW'))
        return func

def print_var(var, name=None):
    """
    Print variable value and type
    Usage:
    from scripts.debug_helper import print_var
    
    x = [1, 2, 3]
    print_var(x, "x")
    """
    if name is None:
        # Try to get variable name
        frame = inspect.currentframe().f_back
        try:
            for var_name, var_val in frame.f_locals.items():
                if var_val is var:
                    name = var_name
                    break
        finally:
            del frame
    
    var_type = type(var).__name__
    print(colorize(f"Variable {name} ({var_type}):", 'BLUE'))
    print(colorize(f"Value: {var}", 'GREEN'))
    
    # If it's a container type, print more information
    if hasattr(var, '__len__'):
        print(colorize(f"Length: {len(var)}", 'CYAN'))
    
    # If it's a dictionary, print keys
    if isinstance(var, dict):
        print(colorize("Keys: ", 'MAGENTA'), list(var.keys()))

def debug_info():
    """
    Print current debugging environment information
    Usage:
    from scripts.debug_helper import debug_info
    
    debug_info()
    """
    print(colorize("\n===== Debugging Environment Info =====", 'CYAN'))
    print(colorize(f"Python version: {sys.version}", 'GREEN'))
    print(colorize(f"Working directory: {os.getcwd()}", 'GREEN'))
    
    # Check if debugging tools are installed
    debug_tools = {
        'ipdb': False,
        'pdb': False,
        'pysnooper': False
    }
    
    try:
        import ipdb
        debug_tools['ipdb'] = True
    except ImportError:
        pass
    
    try:
        import pdb
        debug_tools['pdb'] = True
    except ImportError:
        pass
    
    try:
        import pysnooper
        debug_tools['pysnooper'] = True
    except ImportError:
        pass
    
    print(colorize("\nAvailable debugging tools:", 'BLUE'))
    for tool, available in debug_tools.items():
        status = colorize("Installed", 'GREEN') if available else colorize("Not installed", 'RED')
        print(f"- {tool}: {status}")
    
    print(colorize("\nDebugging commands:", 'YELLOW'))
    print("- debug_break(): Insert breakpoint")
    print("- @trace_function: Trace function execution")
    print("- print_var(var): Print variable information")
    print(colorize("======================\n", 'CYAN'))

if __name__ == "__main__":
    debug_info()
    print(colorize("\nExample usage:", 'MAGENTA'))
    print("""
from scripts.debug_helper import debug_break, trace_function, print_var, debug_info

# Print debugging environment info
debug_info()

# Using breakpoints
def example_function():
    x = [1, 2, 3]
    debug_break()  # Code execution will pause here
    y = sum(x)
    return y

# Trace function execution
@trace_function
def calculate_sum(a, b):
    result = a + b
    return result

# Print variable information
data = {"name": "test", "value": 42}
print_var(data, "data")
    """)
