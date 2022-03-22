#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as
a parameter.

Constraints:
    The letter must be set in the variable q
    if no argument is given, set q=""
    If the response body is properly JSON formatted
    and not empty, display the id and name like this:
    [<id>] <name>, Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    Packages requests and sys should be used
    No other package should be imported
"""

import requests
from sys import argv


def main():
    """Send POST request to URL"""
    letter = {'q': ""}
    if len(argv) == 2:
        letter['q'] = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        myjson = r.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if myjson == {}:
            print("No result")
        else:
            print(f"[{myjson.get('id')}] {myjson.get('name')}")


if __name__ == '__main__':
    main()
