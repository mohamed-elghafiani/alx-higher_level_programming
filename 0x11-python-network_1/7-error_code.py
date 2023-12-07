#!/usr/bin/python3
"""Handling urllib.error.HTTPError"""
import requests
import requests.exceptions
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
