#!/usr/bin/python3
"""Takes URL passed as an argument, sends a request
to the URL and displays the decoded response body

Constraints:
    urllib.error.HTTPError exceptions should be handled
    and print: Error code: HTTP StatusCode
    The packages urllib and sys must be used
    No any other package should be imported
    A with statement must be used
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def main():
    """Sends request to URL and display response body"""
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            content = response.read()
    except HTTPError as e:
        print("Error code:", e.code)
    else:
        print(content.decode('utf-8'))


if __name__ == '__main__':
    main()
