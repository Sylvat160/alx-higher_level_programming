#!/bin/bash
# Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -sX DELETE "$1"