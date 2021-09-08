#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response."""
import sys
import requests

if __name__ == '__main__':
    request = requests.get(sys.argv[1])

    if str(request.status_code)[0] == '2':
        print(request.text)
    else:
        print("Error code: {}".format(request.status_code))
