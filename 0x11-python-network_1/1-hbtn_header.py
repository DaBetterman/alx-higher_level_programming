#!/usr/bin/python3
import sys
import urllib.request
"""
A Python script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

url = sys.argv[1]

with urllib.request.urlopen(url) as file:
    headers = file.info()
    print(headers['X-Request-Id'])