#!/usr/bin/python3
"""Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) <= 1:
        d = {"q": ""}
    else:
        d = {"q": sys.argv[1]}

    re = requests.post(url, data=d)
    try:
        data_dict = re.json()
    except:
        print("Not a valid JSON")
    else:
        if len(data_dict) <= 0:
            print("No result")
        else:
            print("[{}] {}".format(data_dict["id"], data_dict["name"]))
