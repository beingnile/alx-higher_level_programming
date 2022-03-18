#!/usr/bin/python3
"""Takes URL and email passed as arguments,
sends a POST request to the URL with the email
as a parameter and the decoded response body

Constraints:
    The packages urllib and sys must be used
    No any other package should be imported
    A with statement must be used
    The email must be sent in the email variable
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def main():
    """Send POST request to URL and display response body"""
    value = {'email': argv[2]}
    data = urlencode(value)
    data = data.encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as response:
        content = response.read()

    print(content.decode('utf-8'))


if __name__ == '__main__':
    main()
