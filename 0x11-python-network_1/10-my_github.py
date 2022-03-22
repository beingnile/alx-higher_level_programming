#!/usr/bin/python3
"""Takes in GitHub credentials (username, password)
and uses the GitHub API to display the id

The first argument will be the username
The second the password (personal access token)
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


def main():
    """Access the ID"""
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    myjson = r.json()
    print(myjson.get('id'))


if __name__ == '__main__':
    main()
