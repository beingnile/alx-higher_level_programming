#!/usr/bin/python3
"""Takes in a URL and sends a GET request
If status code >= 400, prints 'Error code:'
followed by the value of the HTTP status code
"""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    elif r.status_code == 200:
        print(r.text)
