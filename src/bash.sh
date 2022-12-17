#!/bin/bash

# Check python is installed, if not exit with error message to install python3.
if ! [[ -x "$(command -v python3)" ]]
then
  echo "Error: 
    This program requires Python3 to run. Please check out https://wsvincent.com/install-python/ for instalation instructions and combe back once you you it working." >&2
  exit 1

else 
# Create virtual environment
python3 -m venv venv
# Activate virtual environment
source venv/bin/activate
# Install packages to venv
python -m pip install -r requirements.txt
fi


# Execute main.py to run the app
python3 ./main.py