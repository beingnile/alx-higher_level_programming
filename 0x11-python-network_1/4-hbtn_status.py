#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
using the requests package

Constraints:
    The package `requests` must be used
    No any other package should be imported
    The body of the response must be displayed
    like the example below.

Output example:
    ::
        $ ./4-hbtn_status.py | cat -e
        Body response:$
            - type: <class 'str'>$
            - content: OK$
"""
import requests


def main():
    """Send HTTP request to URL"""
    content = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(content.text)}")
    print(f"\t- content: {content.text}")


if __name__ == '__main__':
    main()
