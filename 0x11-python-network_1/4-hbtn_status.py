#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
#     print("\t- utf8 content:", response.decode('utf-8'))
# else:
#     print("Error, ", response.status_code)
