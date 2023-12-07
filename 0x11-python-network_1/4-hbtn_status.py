#!/usr/bin/python3
"""Fetch url -> https://alx-intranet.hbtn.io/status"""
import requests


with requests.get("https://alx-intranet.hbtn.io/status") as res:
    data = res.text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
