# Ruby Technical Interview Environment

This environment provides a complete setup for technical interviews using Ruby, including automated testing, monitoring tools, and a web application framework.

## Environment Setup

1. Install dependencies:
```bash
bundle install
```

2. Project structure:
   - `lib/`: Place your source code here
   - `test/`: Place test cases here
   - `scripts/`: Automation scripts
   - `db/`: Database migrations and data
   - `views/`: Sinatra view templates
   - `public/`: Static assets

## Using Automation Scripts

### Run Tests
```bash
ruby scripts/run_tests.rb
```

### Watch File Changes and Run Tests Automatically
```bash
ruby scripts/watch_tests.rb
```

### Generate Test Template
```bash
ruby scripts/generate_test.rb <class_name>
```

## Web Application (Sinatra)

### Setup Database
```bash
# Create database
bundle exec rake db:create

# Run migrations
bundle exec rake db:migrate
```

### Run Web Server
```bash
ruby scripts/run_api.rb
```

The API will be available at http://localhost:4567

### API Endpoints
- `GET /`: Welcome message
- `GET /items`: List all items
- `GET /items/:id`: Get item by ID
- `POST /items`: Create a new item
- `PUT /items/:id`: Update an item
- `DELETE /items/:id`: Delete an item

## Test Coverage Report

After running tests, a coverage report will be generated. You can view the HTML report with:
```bash
open coverage/index.html
```

## Debugging Tools

This environment provides various debugging tools and helper functions to assist with rapid code debugging:

### Using Built-in Debug Helper Module

```ruby
# Import debug helper module
require_relative 'lib/debug_helper'
include DebugHelper

# Print debugging environment info
debug_info

# Insert a breakpoint in the code
def example_method
  x = [1, 2, 3]
  debug_break  # Code execution will pause here
  y = x.sum
  return y
end

# Trace method execution
trace_method(:calculate_sum) do |a, b|
  result = a + b
  return result
end

# Print detailed variable information
data = {"name" => "test", "value" => 42}
print_var(data, "data")
```

### Recommended Debugging Tools

1. **pry** - Interactive Ruby debugger
   ```ruby
   # Add to Gemfile
gem 'pry'
gem 'pry-byebug'  # Integrates byebug functionality
   ```

2. **byebug** - Lightweight Ruby debugger
   ```ruby
   # Add to Gemfile
gem 'byebug'
   ```

3. **ruby-debug-ide** - VS Code integration
   ```ruby
   # Add to Gemfile
gem 'ruby-debug-ide'
gem 'debase'
   ```
   - Open project in VS Code
   - Set breakpoints
   - Press F5 to start debugging

## Database (ActiveRecord)

This environment uses SQLite with ActiveRecord ORM:

- Configuration: `config/database.yml`
- Migrations: `db/migrate/`
- Models: Defined in `app.rb`

## Technical Interview Tips

1. Use TDD (Test-Driven Development) approach
2. Write test cases before implementing features
3. Keep code clean and concise
4. Pay attention to edge cases and exception handling
5. Consider performance implications of your solution
