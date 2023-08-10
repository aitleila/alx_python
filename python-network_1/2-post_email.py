#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response
"""
import requests
import sys

url = 'https://alu-intranet.hbtn.io/status'
response = requests.post(url('hr@holbertonschool.com'))

print("{}" "{}". format("Your email is: ")(response))