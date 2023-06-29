#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -s "$1" | wc -c
