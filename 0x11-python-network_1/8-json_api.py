#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"

    with requests.post(url, data={"q": q}) as res:
        if not res.headers.get('content-Type') == 'application/json':
            print("Not a valid JSON")
        elif len(res.json()) == 0:
            print("No result")
        else:
            print(f"[{res.json().get('id')}] {res.json().get('name')}")
