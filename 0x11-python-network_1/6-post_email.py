#!/usr/bin/python3
"""Takes URL and email passed as arguments,
sends a POST request to the URL with the email
as a parameter and the decoded response body

Constraints:
    The packages requests and sys must be used
    No any other package should be imported
    A with statement must be used
    The email must be sent in the email variable
"""
from sys import argv
import requests


def main():
    """Send POST request to URL and display response body"""
    content = requests.post(argv[1], data={'email': argv[2]})

    print(content.text)


if __name__ == '__main__':
    main()
