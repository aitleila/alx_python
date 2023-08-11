#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response
"""
import requests
import sys


if len(sys.argv) != 2:
    email={'email':"hr@holbertonschool.com"}
    print("Your email is: ", email)
    sys.exit(1)
req = sys.argv[1]
email={'email':"hr@holbertonschool.com"}
response = requests.post(req, params=email)
x_request_id = response.headers.get('X-Request-Id')
print(x_request_id)
