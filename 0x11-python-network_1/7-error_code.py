#!/usr/bin/python3
"""Handling urllib.error.HTTPError"""
import requests
import requests.exceptions
import sys


if __name__ == "__main__":
    try:
        with requests.get(sys.argv[1]) as res:
            print(res.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.code}")
