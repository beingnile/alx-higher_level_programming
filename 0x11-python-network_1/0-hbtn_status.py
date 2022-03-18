#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status

Constraints:
    The package urllib must be used
    No any other package should be imported
    A with statement must be used
    The body of the response must be displayed
    like the example below.

Example:
    ::
        $ ./0-hbtn_status.py | cat -e
        Body response:$
            - type: <class 'bytes'>$
            - content: b'OK'$
            - utf8 content: OK$
"""
from urllib.request import urlopen, Request


def main():
    """Make HTTP request to URL"""
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == '__main__':
    main()
