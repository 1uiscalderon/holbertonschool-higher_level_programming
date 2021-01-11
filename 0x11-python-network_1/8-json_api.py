#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter."""
from requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    try:
        res = post('http://0.0.0.0:5000/search_user', data={'q': letter})
        user = res.json()
        if not user:
            print('No result')
        else:
            print('[{}] {}'.format(user.get('id'), user.get('name')))
    except Exception:
        print('Not a valid JSON')
