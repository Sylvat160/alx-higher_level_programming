#!/usr/bin/python3
"""Write a Python script that takes your Github credentials (username and
password) and uses the Github API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))
