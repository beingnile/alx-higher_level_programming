#!/usr/bin/python3
"""Lists 10 commits (from themost recent to oldest)
of a repository(first argument) by the user(second argument)

Usage:
    ./100-github_commits.py <repository name> <repository owner>
"""
from sys import argv
import requests


def main():
    url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"

    r = requests.get(url)
    myjson = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                myjson[i].get("sha"),
                myjson[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
