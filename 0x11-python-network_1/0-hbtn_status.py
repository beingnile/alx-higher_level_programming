#!/usr/bin/python3
from urllib.request import urlopen, Request

def main():
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()

    print(content)

if __name__ == '__main__':
    main()
