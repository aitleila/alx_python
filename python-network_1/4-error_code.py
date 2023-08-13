#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response
"""
import requests
import sys
url='https://alu-intranet.hbtn.io/status'
response = requests.get(url)
r = requests.get(url)

if r.status_code(sys) >= 400:
    print("Error code:",response.status_code)
    sys.exit