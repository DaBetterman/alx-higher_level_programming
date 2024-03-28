#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
from sys import argv
import requests


def main(argv):
    """
    A Python script that takes in a URL, sends a
    request to the URL and displays the value of
    the variable X-Request-Id in the response header
    """
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main(argv)
