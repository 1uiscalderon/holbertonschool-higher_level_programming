#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    try:
        res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        user = res.json()
        print(user)
        if not user:
            print('No result')
        else:
            print('[{}] {}'.format(user.get('id'), user.get('name')))
    except Exception:
        print('Not a valid JSON')
