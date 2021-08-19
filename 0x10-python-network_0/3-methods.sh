#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods
curl -sI | grep Allow: | cut -d' ' -f2-
