#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response
"""
import requests
import sys


req = sys.argv[1]
email={'email':"hr@holbertonschool.com"}
response = requests.post(req, params=email)
x_request_id = response.headers.get('X-Request-Id')
print("Your email is: ""Your email is: ", x_request_id)
