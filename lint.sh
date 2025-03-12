
#!/bin/bash

# Format with Black
echo "Running Black formatter..."
black .

# Sort imports
echo "Running isort..."
isort .

# Run static type checking
echo "Running mypy..."
mypy app.py

# Run pylint
echo "Running pylint..."
pylint app.py

# Run flake8
echo "Running flake8..."
flake8 app.py

# Run tests
echo "Running pytest..."
pytest -v

echo "All checks completed!"
