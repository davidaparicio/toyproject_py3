#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

## OR if it's in edition (dev/watch mode)
# pip install -e .

# Additional setup steps can be added here, like database migrations or generating docs
echo "Project setup complete and virtual environment activated!"
