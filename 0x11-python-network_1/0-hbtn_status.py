#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            print("Body response:")
            print(f"\t- type: {type(res)}")
            print(f"\t- content: {res}")
            print(f"\t- utf8 content: {response.msg}")
    except Exception:
        pass
