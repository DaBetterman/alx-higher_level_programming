#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import urllib.request
from sys import argv


def main(argv):
    """
    A Python script that takes in a URL, sends a request
    to the URL and displays the body of the response
    (decoded in utf-8).
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as file:
            result = file.read()
            print(result.decode('utf8'))
    except urllib.error.URLError as message:
        print("Error code: {}".format(message.code))


if __name__ == "__main__":
    main(argv)