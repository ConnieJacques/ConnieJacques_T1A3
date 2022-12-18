#!/bin/bash

if command -v python3 &> /dev/null
then
    # Execute main.py to run the app
    python3 src/main.py
    exit
fi