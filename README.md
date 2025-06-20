# Technical Interview Environment

This project provides a coding environment for technical interviews, including automated testing and monitoring tools.

## Project Structure

```
.
├── README.md                 # Project documentation
├── python_env/               # Python environment
│   ├── src/                  # Source code directory
│   │   ├── models.py         # Database models
│   │   └── database.py       # Database connection
│   ├── tests/                # Test directory
│   ├── requirements.txt      # Dependency management
│   └── scripts/              # Automation scripts
│       ├── run_tests.py      # Run tests once
│       └── watch_tests.py    # Watch files and run tests
└── ruby_env/                 # Ruby environment
    ├── lib/                  # Source code directory
    ├── test/                 # Test directory
    ├── app.rb                # Sinatra API application
    ├── db/                   # Database migrations
    ├── Gemfile               # Dependency management
    └── scripts/              # Automation scripts
        ├── run_tests.rb      # Run tests once
        ├── watch_tests.rb    # Watch files and run tests
        └── run_api.rb        # Run Sinatra API server
```

## Usage Instructions

1. Choose your preferred language environment (Python or Ruby)
2. Write code in the corresponding directory
3. Use automation scripts to run tests

### Python Environment

```bash
# Install dependencies
pip install -r python_env/requirements.txt

# Run tests once
python python_env/scripts/run_tests.py

# Watch files and run tests automatically
python python_env/scripts/watch_tests.py

# Generate test template for a module
python python_env/scripts/generate_test.py <module_name>
# Example: python python_env/scripts/generate_test.py calculator
```

### Ruby Environment

```bash
# Install dependencies
cd ruby_env
bundle install

# Run tests once
ruby scripts/run_tests.rb

# Watch files and run tests automatically
ruby scripts/watch_tests.rb

# Run Sinatra API server
ruby scripts/run_api.rb

# Generate test template for a class
ruby scripts/generate_test.rb <class_name>
# Example: ruby scripts/generate_test.rb Calculator
```

For detailed instructions, please refer to the README files in each environment directory.

## Sample Interview Problems

This environment includes several sample interview problems to help you practice:

1. **String Reversal (Easy)** - Implementation of StringUtils.reverse_string method
2. **Palindrome Detection (Medium)** - Implementation of StringUtils.is_palindrome method that ignores case, spaces, and punctuation
3. **Longest Common Subsequence (Medium-Hard)** - Implementation of SequenceUtils.longest_common_subsequence method using dynamic programming

Each problem has complete implementations and test cases in both Python and Ruby environments.

## Test Coverage Reports

### Python Coverage Report
After running tests, view the HTML coverage report at:
```bash
open python_env/htmlcov/index.html
```

### Ruby Coverage Report
After running tests, view the HTML coverage report at:
```bash
open ruby_env/coverage/index.html
```
