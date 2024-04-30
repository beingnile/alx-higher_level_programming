#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url).text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
