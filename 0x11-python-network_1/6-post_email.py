#!/usr/bin/python3
"""Takes in a URL and email address and sends a POST request
to the URL with the passed email as value for 'email'
"""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
