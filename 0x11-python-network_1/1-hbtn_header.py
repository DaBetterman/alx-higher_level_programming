#!/usr/bin/python3
from sys import argv
import urllib.request


def main(argv):
    """
    A Python script that takes in a URL, sends a request to
    the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
    """
    url = argv
    with urllib.request.urlopen(url) as file:
        headers = file.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
