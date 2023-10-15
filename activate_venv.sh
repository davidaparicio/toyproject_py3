#!/bin/bash

source venv/bin/activate

# Append the current directory to PYTHONPATH
export PYTHONPATH="$PWD/my_project:$PYTHONPATH"
echo $PYTHONPATH

#if [ -e ./venv/bin/activate ]; then source ./venv/bin/activate; else python3 -m venv venv && source ./venv/bin/activate; fi

#python -c "import sys; print(sys.path)"
#deactivate             # If the virtual environment is active
#rm -rf venv/           # Delete the existing virtual environment
#python3 -m venv venv   # Create a new virtual environment
#source venv/bin/activate  # Activate the virtual environment