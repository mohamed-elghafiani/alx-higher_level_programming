#!/usr/bin/python3
"""Handling urllib.error.HTTPError"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request('http://www.python.org/fish.html')
    try:
        body = urllib.request.urlopen(req)
        print(body.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
