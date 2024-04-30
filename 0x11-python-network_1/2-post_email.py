#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the response body (decoded in utf-8)
"""
if __name__ == '__main__':
    from sys import argv
    import urllib.request
    import urllib.parse

    values = { "email": argv[2] }
    url = argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
