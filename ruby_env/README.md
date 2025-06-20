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
