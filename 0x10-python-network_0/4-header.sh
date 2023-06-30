#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"