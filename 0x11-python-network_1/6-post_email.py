#!/usr/bin/python3
"""Post an email"""
import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]
    data = {'email': argv[2]}

    with requests.post(url, data) as response:
        print(response.text)
