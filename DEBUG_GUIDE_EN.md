# Python and Ruby Debugging Guide

This document provides detailed steps and methods for debugging Python and Ruby code in the development environment. We will introduce various debugging techniques, from simple print debugging to using professional debugging tools.

## Table of Contents

- [Python Debugging Guide](#python-debugging-guide)
  - [Basic Debugging Techniques](#python-basic-debugging-techniques)
  - [Using Built-in Debug Helper Module](#python-using-built-in-debug-helper-module)
  - [Using pdb/ipdb Debugger](#using-pdbipdb-debugger)
  - [Using PySnooper for Non-intrusive Debugging](#using-pysnooper-for-non-intrusive-debugging)
  - [Using VS Code for Graphical Debugging](#python-using-vs-code-for-graphical-debugging)
- [Ruby Debugging Guide](#ruby-debugging-guide)
  - [Basic Debugging Techniques](#ruby-basic-debugging-techniques)
  - [Using Built-in Debug Helper Module](#ruby-using-built-in-debug-helper-module)
  - [Using pry and byebug Debuggers](#using-pry-and-byebug-debuggers)
  - [Using VS Code for Graphical Debugging](#ruby-using-vs-code-for-graphical-debugging)

## Python Debugging Guide

### Python Basic Debugging Techniques

#### 1. Using print Statements

The simplest debugging method is to use `print` statements to output variable values:

```python
def calculate_sum(a, b):
    print(f"a = {a}, b = {b}")
    result = a + b
    print(f"Result: {result}")
    return result
```

#### 2. Using the logging Module

A more flexible method than print is to use Python's `logging` module:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

def calculate_sum(a, b):
    logging.debug(f"a = {a}, b = {b}")
    result = a + b
    logging.info(f"Calculation result: {result}")
    return result
```

### Python Using Built-in Debug Helper Module

Our environment provides a dedicated debugging helper module, located at `scripts/debug_helper.py`, which includes various useful debugging functions:

#### 1. Importing the Debug Helper Module

```python
from scripts.debug_helper import debug_break, trace_function, print_var, debug_info
```

#### 2. Viewing Debug Environment Information

```python
# Print information about debugging tools in the current environment
debug_info()
```

#### 3. Inserting Breakpoints in Code

```python
def example_function():
    x = [1, 2, 3]
    debug_break()  # Code execution will pause here
    y = sum(x)
    return y
```

#### 4. Tracing Function Execution

Use a decorator to track variable changes during function execution:

```python
@trace_function
def calculate_sum(a, b):
    result = a + b
    return result
```

#### 5. Printing Detailed Variable Information

```python
data = {"name": "test", "value": 42, "items": [1, 2, 3]}
print_var(data, "data")  # Will display variable type, value, length, etc.
```

### Using pdb/ipdb Debugger

pdb is Python's built-in debugger, and ipdb is its enhanced version, providing syntax highlighting and tab completion.

#### 1. Installing ipdb

```bash
pip install ipdb
```

#### 2. Inserting Breakpoints in Code

```python
import ipdb

def problematic_function():
    x = 10
    y = 0
    ipdb.set_trace()  # Code execution will pause here
    result = x / y  # This will cause a division by zero error
    return result
```

#### 3. Common Debugging Commands

- `n` (next): Execute the current line and move to the next line
- `s` (step): Step through execution; if the current line calls a function, step into that function
- `c` (continue): Continue execution until the next breakpoint
- `q` (quit): Exit the debugger
- `p variable_name`: Print the variable value
- `pp variable_name`: Format and print the variable value
- `l` (list): Display code around the current line
- `w` (where): Print the current call stack

### Using PySnooper for Non-intrusive Debugging

PySnooper is a very convenient debugging tool that can record variable changes during function execution.

#### 1. Installing PySnooper

```bash
pip install pysnooper
```

#### 2. Using PySnooper to Trace Function Execution

```python
import pysnooper

@pysnooper.snoop()
def calculate_division(a, b):
    result = a / b
    return result

calculate_division(10, 2)  # Will output each step of function execution and variable changes
```

#### 3. Saving Debug Logs to a File

```python
@pysnooper.snoop('/tmp/debug_log.log')
def complex_function():
    # Function code
    pass
```

### Python Using VS Code for Graphical Debugging

VS Code provides powerful graphical debugging capabilities, particularly suitable for complex project debugging.

#### 1. Configuring VS Code

1. Install the Python extension: Search for and install the "Python" extension in the VS Code extension marketplace
2. Create a `.vscode/launch.json` file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

#### 2. Setting Breakpoints

1. Click on the left side of the line number to set a breakpoint (a red dot will appear)
2. Or add a `breakpoint()` statement in the code (Python 3.7+)

#### 3. Starting Debugging

1. Open the Python file you want to debug
2. Press F5 or click the start button in the debug panel
3. The program will pause execution at the breakpoint

#### 4. Debug Controls

- Continue execution (F5)
- Step over (F10)
- Step into (F11)
- Step out (Shift+F11)
- Restart (Ctrl+Shift+F5)
- Stop (Shift+F5)

## Ruby Debugging Guide

### Ruby Basic Debugging Techniques

#### 1. Using puts Statements

The simplest debugging method is to use `puts` statements to output variable values:

```ruby
def calculate_sum(a, b)
  puts "a = #{a}, b = #{b}"
  result = a + b
  puts "Result: #{result}"
  result
end
```

#### 2. Using the pp Method

For complex data structures, you can use the `pp` (pretty print) method:

```ruby
require 'pp'

def inspect_data(data)
  pp data  # Format and print data
  # Process data...
end
```

### Ruby Using Built-in Debug Helper Module

Our environment provides a dedicated debugging helper module, located at `lib/debug_helper.rb`, which includes various useful debugging functions:

#### 1. Importing the Debug Helper Module

```ruby
require_relative 'lib/debug_helper'
include DebugHelper
```

#### 2. Viewing Debug Environment Information

```ruby
# Print information about debugging tools in the current environment
debug_info
```

#### 3. Inserting Breakpoints in Code

```ruby
def example_method
  x = [1, 2, 3]
  debug_break  # Code execution will pause here
  y = x.sum
  return y
end
```

#### 4. Tracing Method Execution

```ruby
trace_method(:calculate_sum) do |a, b|
  result = a + b
  return result
end
```

#### 5. Printing Detailed Variable Information

```ruby
data = {"name" => "test", "value" => 42, "items" => [1, 2, 3]}
print_var(data, "data")  # Will display variable type, value, length, etc.
```

### Using pry and byebug Debuggers

pry is Ruby's interactive debugger, and byebug is another powerful debugger. The two can be used together.

#### 1. Installing Debuggers

Add to your Gemfile:

```ruby
gem 'pry'
gem 'byebug'
gem 'pry-byebug'  # Integrates pry and byebug
```

Then run:

```bash
bundle install
```

#### 2. Inserting Breakpoints in Code

```ruby
require 'pry'

def problematic_method
  x = 10
  y = 0
  binding.pry  # Code execution will pause here
  result = x / y  # This will cause a division by zero error
  result
end
```

Or using byebug:

```ruby
require 'byebug'

def problematic_method
  x = 10
  y = 0
  byebug  # Code execution will pause here
  result = x / y  # This will cause a division by zero error
  result
end
```

#### 3. Common Debugging Commands

Pry commands:
- `next` or `n`: Execute the current line and move to the next line
- `step` or `s`: Step through execution; if the current line calls a method, step into that method
- `continue` or `c`: Continue execution until the next breakpoint
- `exit` or `quit`: Exit the debugger
- `whereami`: Show code at the current location
- `help`: Display help information

Byebug commands:
- `next` or `n`: Execute the current line and move to the next line
- `step` or `s`: Step through execution, step into methods
- `continue` or `c`: Continue execution
- `quit` or `q`: Exit the debugger
- `display variable_name`: Display the variable value each time execution stops
- `undisplay`: Cancel variable display

### Ruby Using VS Code for Graphical Debugging

VS Code also supports graphical debugging for Ruby.

#### 1. Configuring VS Code

1. Install the Ruby extension: Search for and install the "Ruby" extension in the VS Code extension marketplace
2. Install necessary gems:

```ruby
gem 'ruby-debug-ide'
gem 'debase'
```

3. Create a `.vscode/launch.json` file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Ruby",
            "type": "Ruby",
            "request": "launch",
            "program": "${file}",
            "useBundler": true
        }
    ]
}
```

#### 2. Setting Breakpoints

1. Click on the left side of the line number to set a breakpoint (a red dot will appear)

#### 3. Starting Debugging

1. Open the Ruby file you want to debug
2. Press F5 or click the start button in the debug panel
3. The program will pause execution at the breakpoint

#### 4. Debug Controls

- Continue execution (F5)
- Step over (F10)
- Step into (F11)
- Step out (Shift+F11)
- Restart (Ctrl+Shift+F5)
- Stop (Shift+F5)

## Debugging Best Practices

1. **Start Simple**: First use simple print/puts statements; if the problem persists, then use more advanced debugging tools
2. **Isolate the Problem**: Try to create a minimal example to reproduce the issue
3. **Check Data Types**: Many errors are caused by mismatched data types
4. **Use Version Control**: Before making major debugging changes, ensure your code is committed to a version control system
5. **Document the Debugging Process**: Record the methods you've tried and the issues you've found to avoid duplicating work
6. **Use Assertions**: Add assertions to your code to validate assumptions
7. **Check Boundary Conditions**: Pay special attention to boundary conditions, such as empty values, zero values, extremely large values, etc.

## Common Troubleshooting

### Python Common Issues

1. **ImportError/ModuleNotFoundError**: Check module paths and the PYTHONPATH environment variable
2. **IndentationError**: Check code indentation; Python is very sensitive to indentation
3. **TypeError**: Check variable types, especially during function calls
4. **IndexError/KeyError**: Check if list indices or dictionary keys exist
5. **AttributeError**: Check if the object has the attribute or method

### Ruby Common Issues

1. **NameError**: Check if variables or constants are defined
2. **NoMethodError**: Check if the object has the method
3. **ArgumentError**: Check if the method call has the correct number of arguments
4. **TypeError**: Check if variable types meet expectations
5. **LoadError**: Check if the require file path is correct

## Conclusion

This guide covers the essential debugging techniques for Python and Ruby development. By mastering these tools and methods, you can significantly improve your debugging efficiency and code quality. Remember that debugging is not just about fixing errors but also about understanding how your code works.

For more specific debugging needs or advanced techniques, please refer to the official documentation for each tool or consult with your team's technical lead.
