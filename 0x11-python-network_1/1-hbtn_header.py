#!/usr/bin/python3
import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as file:
    if 'X-Request-Id' in file.headers:
        print(file.headers['X-Request-Id'])
    else:
        print("not found")
