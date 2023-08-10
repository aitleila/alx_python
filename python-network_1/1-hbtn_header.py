#!/usr/bin/python3
"""
Make a HEAD request to a web page, and return the HTTP headers
"""
import requests

req = 'https://intranet.hbtn.io'
response = requests.head(req)

print(response)