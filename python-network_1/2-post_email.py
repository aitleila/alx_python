#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response
"""
import requests
import sys


if len(sys.argv) != 2:
    email="test@test"
    print("Email: ", email)
    sys.exit(1)

req = sys.argv[1]
response = requests.get(req)
x_request_id = response.headers.get('X-Request-Id')
print(x_request_id)

