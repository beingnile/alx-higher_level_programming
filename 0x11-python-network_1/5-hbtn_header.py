#!/usr/bin/python3
"""Sends a get request to a passed URL and prints
an header value
"""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
