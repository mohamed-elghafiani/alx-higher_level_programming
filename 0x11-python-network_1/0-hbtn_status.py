#!/usr/bin/python3
"""Fetch url -> https://alx-intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    data = res.read()
    print(f"""Body response:
    - {type(data)}
    - {data}
    - {data.decode("utf-8")}""")
