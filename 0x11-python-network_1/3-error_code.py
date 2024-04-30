#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the response body"""
if __name__ == '__main__':
    from sys import argv
    import urllib.request

    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
