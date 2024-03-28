#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


def main(argv):
    """
    A Python script that takes in a URL, sends a
    request to the URL and displays the body of the response.
    """
    url = argv[1]
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    main(argv)
