#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
from sys import argv
import requests


def main(argv):
    """
    A Python script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email
    as a parameter, and finally displays the body of the response.
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, values)
    print(r.text)


if __name__ == "__main__":
    main(argv)
