#!/bin/bash

# Evaluates to True if Python is installed and false otherwise
if ! [[ -x "$(command -v python3)" ]]
then 
    echo 'Error:
        This program runs on Python3. It looks like you either dont have Python installed or have an outdated version. To install Python, you can run: "sudo apt install python3-pip" or check your version with: "pip3 --version"' >&2
    exit 1
fi

# Run main.py module
python3 main.py