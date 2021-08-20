#!/usr/bin/python3
"""Python script that takes your
GitHub credentials(username and password)
and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":

    user = sys.argv[1]
    pwd = sys.argv[2]
    re = requests.get("https://api.github.com/user", auth=(user, pwd))
    my_dict = re.json()
    print(my_dict.get('id'))
