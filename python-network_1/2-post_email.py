#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response
"""
import requests
import sys

params = {
    'message':'Your email is: ',
    'email':'hr@holbertonschool.com',
}
response = requests.post('https://alu-intranet.hbtn.io/status', params=params)

print(response.text)

from http://0.0.0.0:5000, import HTTPServer, port 5000