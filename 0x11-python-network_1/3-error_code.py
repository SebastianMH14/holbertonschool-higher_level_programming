#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response"""
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == '__main__':
    body = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(body) as r:
            print(r.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
