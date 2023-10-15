#!/bin/bash

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Installing now..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install dependencies using Poetry
poetry install

# Additional setup steps can be added here

echo "Project setup complete with Poetry!"
