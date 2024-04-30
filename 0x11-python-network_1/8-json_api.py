#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    r = requests.post(url, data={'q': q})
    try:
        res = r.json()
        if res:
            print(f"[{res.get('id')}] {res.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
