#!/usr/bin/python3
"""Python script that takes 2 arguments in order to list 10 commits
(from the most recent to oldest) of a repository"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1]))
    for i in req.json()[0:10]:
        print("{}: {}".format(i.get("sha"),
                              i.get("commit").get("author").get("name")))
