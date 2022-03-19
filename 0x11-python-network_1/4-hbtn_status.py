#!/usr/bin/python3
"""The module fetches a URL"""
import requests


def main():
    """Send HTTP request to URL"""
    content = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(content.text)}")
    print(f"\t- content: {content.text}")


if __name__ == '__main__':
    main()
