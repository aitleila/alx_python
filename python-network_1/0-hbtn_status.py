"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
req = requests.get('https://alu-intranet.hbtn.io/status')
response = req
print ("Body response:")
print(f"\t- type:{type(response.text)}")
print(f"\t- content:{response.text}")

