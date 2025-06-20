# Python Technical Interview Environment

This environment provides a complete setup for technical interviews using Python, including automated testing, monitoring tools, and a web application framework.

## Environment Setup

1. Install dependencies:
```bash
# Method 1: Install directly with pip
pip install -r requirements.txt

# Method 2: Use installation script (recommended)
python scripts/install_dependencies.py
```

2. Project structure:
   - `src/`: Place your source code here
   - `tests/`: Place test cases here
   - `scripts/`: Automation scripts

## Using Automation Scripts

### Run Tests
```bash
python scripts/run_tests.py
```

### Watch File Changes and Run Tests Automatically
```bash
python scripts/watch_tests.py
```

### Generate Test Template
```bash
python scripts/generate_test.py <module_name>
```

## Web Application (FastAPI)

### Run Web Server
```bash
python scripts/run_api.py
```

The FastAPI server will start at http://127.0.0.1:8000

### API Documentation
FastAPI automatically generates interactive API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Test Coverage Report

After running tests, a coverage report will be generated. You can view the HTML report with:
```bash
open htmlcov/index.html
```

## Debugging Tools

This environment provides various debugging tools and helper functions to assist with rapid code debugging:

### Using Built-in Debug Helper Module

```python
# Import debug helper module
from scripts.debug_helper import debug_break, trace_function, print_var, debug_info

# Print debugging environment info
debug_info()

# Insert a breakpoint in the code
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

# Print detailed variable information
data = {"name": "test", "value": 42}
print_var(data, "data")
```

### Recommended Debugging Tools

1. **ipdb/pdb** - Interactive debugger
   ```bash
   pip install ipdb
   ```

2. **PySnooper** - Non-intrusive debugging tool
   ```bash
   pip install pysnooper
   ```

3. **VS Code Debugger** - Graphical interface debugging
   - Open project in VS Code
   - Set breakpoints
   - Press F5 to start debugging

### API Endpoints
- `GET /`: Welcome message
- `GET /items/`: List all items
- `GET /items/{item_id}`: Get item by ID
- `POST /items/`: Create a new item
- `DELETE /items/{item_id}`: Delete an item

## Database (SQLAlchemy)

This environment uses SQLite with SQLAlchemy ORM:

- Database configuration: `src/database.py`
- Models: `src/models.py`
- Database file: `interview.db` (created automatically)

## Technical Interview Tips

1. Use TDD (Test-Driven Development) approach
2. Write test cases before implementing features
3. Keep code clean and concise
4. Pay attention to edge cases and exception handling
5. Consider performance implications of your solution
