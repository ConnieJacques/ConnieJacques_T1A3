#!/bin/bash

echo "Welcome to The Quz Game. Let's get you set up."
sleep 1

# Check python is installed, if not exit with error message to install python3.
if ! [[ -x "$(command -v python3)" ]]
then
  echo "Error: 
  This program requires Python3 to run. Please check out https://wsvincent.com/install-python/ for instalation instructions and combe back once you you it working." >&2
  exit 1
fi

if [[ -x "$(command -v python3)" ]] &> /dev/null
then
  echo "Creating a virtual environment..."
  # Create virtual environment
  python3 -m venv venv
  sleep 1
  echo "Activating venv..."
  # Activate virtual environment
  source venv/bin/activate
  sleep 1
  echo "Installing requirements to run The Quiz Game..."
  # Install packages to venv
  pip3 install -r requirements.txt
  sleep 1
  echo "Starting up The Quiz Game..."
  sleep 1
  ./rungame.sh
  exit
fi
