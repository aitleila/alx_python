#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response
"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <https://alu-intranet.hbtn.io/status>")
    sys.exit(1)

url = 'https://alu-intranet.hbtn.io/status'
email={'email':"hr@holbertonschool.com"}
response = requests.post(url, params=email)

print("Your email is: ", response)


