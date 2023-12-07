#!/usr/bin/python3
# Response header value
"""
A Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    with requests.get(argv[1]) as req:
        x_request_id = req.headers.get("X-Request-Id")
        print(x_request_id)
