#!/usr/bin/python3
"""Send request to URL passed as argument and display value of the
X-Request-Id variable found in the reponse header

Constraints:
    The packages requests and sys must be used
    No any other package should be imported
"""
import requests
from sys import argv


def main():
    """Send HTTP request to URL and display X-Request-Id value"""
    content = requests.get(argv[1])
    print(content.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
