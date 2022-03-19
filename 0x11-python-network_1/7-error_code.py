#!/usr/bin/python3
"""Takes URL passed as an argument, sends a request
to the URL and displays the decoded response body

Constraints:
    If the HTTP status code >= 400,
    print: Error code: HTTP StatusCode
    The packages requests and sys must be used
    No any other package should be imported
    A with statement must be used
"""
from sys import argv
import requests


def main():
    """Sends request to URL and display response body"""
    content = requests.get(argv[1])
    if content.status_code >= 400:
        print("Error code:", content.status_code)
    else:
        print(content.text)


if __name__ == '__main__':
    main()
