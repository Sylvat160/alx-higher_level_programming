#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http//0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {"q": letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
