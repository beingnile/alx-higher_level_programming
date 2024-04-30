#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the value of X-Request-Id found in the response header
"""
if __name__ == '__main__':
    from sys import argv
    import urllib.request

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.getheaders()).get('X-Request-Id'))
