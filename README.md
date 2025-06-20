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
```

For detailed instructions, please refer to the README files in each environment directory.
