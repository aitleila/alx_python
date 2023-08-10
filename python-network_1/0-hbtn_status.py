"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
req = requests.get('https://alu-intranet.hbtn.io/status')
print (req.text)
