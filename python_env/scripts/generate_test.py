#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script for automatically generating test templates
"""

import os
import sys
import inspect
import importlib
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


def generate_test_template(module_name):
    """
    Generate test template for the specified module
    
    Args:
        module_name: Module name, e.g. 'calculator' or 'src.calculator'
    
    Returns:
        bool: Whether the test was successfully generated
    """
    print(colorize("\n" + "="*50, 'CYAN'))
    print(colorize("GENERATE TEST".center(50), 'CYAN'))
    print(colorize("="*50 + "\n", 'CYAN'))
    
    try:
        # If no full path provided, assume it's in the src directory
        if '.' not in module_name:
            module_name = f"src.{module_name}"
        
        print(colorize(f"Generating test template for module {module_name}...", 'GREEN'))
        
        # Try to import the module
        module = importlib.import_module(module_name)
        
        # Get all classes in the module
        classes = inspect.getmembers(module, inspect.isclass)
        
        if not classes:
            print(colorize(f"Warning: No classes found in module {module_name}", 'YELLOW'))
            return False
        
        # Generate test file for each class
        for class_name, class_obj in classes:
            # Skip imported classes
            if class_obj.__module__ != module.__name__:
                continue
            
            # Determine test file path
            test_file_name = f"test_{module_name.split('.')[-1]}_{class_name.lower()}.py"
            test_file_path = Path("tests") / test_file_name
            
            # If test file already exists, ask whether to overwrite
            if test_file_path.exists():
                print(colorize(f"Test file {test_file_path} already exists.", 'YELLOW'))
                choice = input(colorize("Overwrite? (y/n): ", 'YELLOW')).strip().lower()
                if choice != 'y':
                    continue
            
            # Get all methods of the class
            methods = inspect.getmembers(class_obj, inspect.isfunction)
            
            # Generate test class content
            test_content = [
                f"#!/usr/bin/env python",
                f"# -*- coding: utf-8 -*-",
                f"\"\"\"",
                f"Tests for {module_name}.{class_name} class",
                f"\"\"\"",
                f"",
                f"import unittest",
                f"from {module_name} import {class_name}",
                f"",
                f"",
                f"class Test{class_name}(unittest.TestCase):",
                f"    \"\"\"",
                f"    Tests for the functionality of {class_name} class",
                f"    \"\"\"",
                f"",
                f"    def setUp(self):",
                f"        \"\"\"",
                f"        Setup before each test method",
                f"        \"\"\"",
                f"        self.instance = {class_name}()",
                f"",
            ]
            
            # Generate test methods for each method
            for method_name, method_obj in methods:
                # Skip private methods and special methods
                if method_name.startswith('_'):
                    continue
                
                test_content.extend([
                    f"    def test_{method_name}(self):",
                    f"        \"\"\"",
                    f"        Test the {method_name} method",
                    f"        \"\"\"",
                    f"        # TODO: Implement test cases",
                    f"        self.assertTrue(True)  # Replace with actual tests",
                    f"",
                ])
            
            # Add main function
            test_content.extend([
                f"",
                f"if __name__ == '__main__':",
                f"    unittest.main()",
            ])
            
            # Write test file
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(test_content))
            
            print(colorize(f"Generated test file: {test_file_path}", 'GREEN'))
        
        return True
    
    except ImportError:
        print(colorize(f"Error: Could not import module {module_name}", 'RED'))
        print(colorize("Make sure the module exists and can be imported", 'YELLOW'))
        return False
    
    except Exception as e:
        print(colorize(f"Error occurred while generating test template: {e}", 'RED'))
        return False


def create_example_module():
    """
    Create an example module for demonstration
    """
    src_dir = Path("src")
    if not src_dir.exists():
        src_dir.mkdir(parents=True, exist_ok=True)
        print(colorize(f"Created directory: {src_dir}", 'MAGENTA'))
    
    # Create __init__.py
    init_file = src_dir / "__init__.py"
    if not init_file.exists():
        init_file.touch()
        print(colorize(f"Created file: {init_file}", 'BLUE'))
    
    # Create example module
    example_file = src_dir / "calculator.py"
    
    example_content = [
        "#!/usr/bin/env python",
        "# -*- coding: utf-8 -*-",
        "\"\"\"",
        "Simple calculator module example",
        "\"\"\"",
        "",
        "",
        "class Calculator:",
        "    \"\"\"",
        "    Calculator class implementing basic mathematical operations",
        "    \"\"\"",
        "",
        "    def add(self, a, b):",
        "        \"\"\"",
        "        Calculate the sum of two numbers",
        "        ",
        "        Args:",
        "            a: First number",
        "            b: Second number",
        "        ",
        "        Returns:",
        "            Sum of the two numbers",
        "        \"\"\"",
        "        return a + b",
        "",
        "    def subtract(self, a, b):",
        "        \"\"\"",
        "        Calculate the difference between two numbers",
        "        ",
        "        Args:",
        "            a: First number",
        "            b: Second number",
        "        ",
        "        Returns:",
        "            Difference between the two numbers",
        "        \"\"\"",
        "        return a - b",
        "",
        "    def multiply(self, a, b):",
        "        \"\"\"",
        "        Calculate the product of two numbers",
        "        ",
        "        Args:",
        "            a: First number",
        "            b: Second number",
        "        ",
        "        Returns:",
        "            Product of the two numbers",
        "        \"\"\"",
        "        return a * b",
        "",
        "    def divide(self, a, b):",
        "        \"\"\"",
        "        Calculate the quotient of two numbers",
        "        ",
        "        Args:",
        "            a: First number",
        "            b: Second number",
        "        ",
        "        Returns:",
        "            Quotient of the two numbers",
        "        ",
        "        Raises:",
        "            ZeroDivisionError: When the divisor is zero",
        "        \"\"\"",
        "        if b == 0:",
        "            raise ZeroDivisionError(\"Divisor cannot be zero\")",
        "        return a / b",
    ]
    
    with open(example_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(example_content))
    
    print(colorize(f"Created example module: {example_file}", 'GREEN'))


if __name__ == "__main__":
    # Change to project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # If no module name provided, show usage instructions
    if len(sys.argv) < 2:
        print(colorize("Usage: python generate_test.py <module_name>", 'YELLOW'))
        print(colorize("Example: python generate_test.py calculator", 'BLUE'))
        print(colorize("\nCreating example module...", 'MAGENTA'))
        create_example_module()
        sys.exit(1)
    
    # Generate test template
    module_name = sys.argv[1]
    success = generate_test_template(module_name)
    
    if success:
        print(colorize(f"\nSuccessfully generated test template for module {module_name}", 'GREEN'))
    else:
        print(colorize(f"\nFailed to generate test template for module {module_name}", 'RED'))
