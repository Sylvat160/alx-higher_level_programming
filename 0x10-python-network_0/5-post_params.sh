#!/bin/bash

# Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"