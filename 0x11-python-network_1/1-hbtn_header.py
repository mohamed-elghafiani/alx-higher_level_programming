#!/usr/bin/python3
# Response header value
"""A Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


argv = sys.argv
with urllib.request.urlopen(argv[1]) as req:
    x_request_id = dict(req.headers._headers)["X-Request-Id"]
    print(x_request_id)
