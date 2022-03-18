#!/usr/bin/python3
"""Send request to URL and display value of the
X-Request-Id variable found in the reponse header

Constraints:
    The packages urllib and sys must be used
    No any other package should be imported
    A with statement must be used
"""
from sys import argv
from urllib.request import urlopen, Request


def main():
    """Send HTTP request to URL and display X-Request-Id value"""
    req = Request(argv[1])
    with urlopen(req) as response:
        val = response.info()

    print(val.get("X-Request-Id"))


if __name__ == '__main__':
    main()
