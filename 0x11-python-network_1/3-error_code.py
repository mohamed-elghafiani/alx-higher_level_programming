#!/usr/bin/python3
"""Handling urllib.error.HTTPError"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(arg[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
