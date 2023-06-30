#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8)."""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
