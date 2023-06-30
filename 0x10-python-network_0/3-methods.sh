#!/bin/bash

# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -sI "$1" | awk '/Allow/ {print $2}' | cut -d " " -f 2-