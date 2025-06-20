# Python Technical Interview Environment

This environment provides a complete setup for technical interviews using Python, including automated testing, monitoring tools, and a web application framework.

## Environment Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
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

The API will be available at http://127.0.0.1:8000

### API Documentation
FastAPI automatically generates interactive API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

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
