#!/usr/bin/python3
import urllib.request
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as file:
    body = file.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
