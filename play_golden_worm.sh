#!/bin/bash

# Evaluates to True if Python is installed and false otherwise
if ! [[ -x "$(command -v python3)" ]]
then 
    echo 'Error:
        This program runs on Python3.10. It looks like you either dont have Python installed or have an outdated version. To install Python, you can run: "sudo apt install python3.10" or check your version with: "pip3 --version"' >&2
    exit 1
fi

# Install Packages
python3 -m pip install -r requirements.txt

# Run main.py module
python3 main.py