#!/usr/bin/python3
"""Post an email"""
import urllib.request
import sys


if __name__ == "__main__":
    argv = sys.argv
    url = argv[0]
    values = {'email' : argv[1]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
       body = response.read()
       print(f"Your email is: {body.decode('utf-8')}")
