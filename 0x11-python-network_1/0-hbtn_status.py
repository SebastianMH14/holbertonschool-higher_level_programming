#!/usr/bin/python3
""" Python script that fetches
https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as r:
        display = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(display)))
        print("\t- content: {}".format(display))
        print("\t- utf8 content: {}".format(display.decode(encoding="utf-8")))
