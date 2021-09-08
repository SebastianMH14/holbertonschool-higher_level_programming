#!/usr/bin/python3
"""Python script that takes in a URL
and an email, sends a POST request"""
import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    dic_value = {'email': email}

    data = urllib.parse.urlencode(dic_value)
    data = data.encode()
    r_data = urllib.request.Request(url, data)
    with urllib.request.urlopen(r_data) as r:
        fin = r.read()
        fin = fin.decode('utf-8')
        print(fin)
