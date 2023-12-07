#!/usr/bin/python3
"""
    Search API
"""
import requests
import sys


q = "" if len(sys.argv) < 2 else sys.argv[1]
url = "http://0.0.0.0:5000/search_user"

with requests.post(url, params={"q": q}) as res:
    if not res.headers.get('content-Type') == 'application/json':
        print("Not a validd JSON")
    elif res.json() == {}:
        print("No result")
    else:
        print(res.json())
        print(f"[{res.json().get('id')}] {res.json().get('name')}")
