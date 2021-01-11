#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    email = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode("utf-8"))
