import requests

"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""

req = requests.get('https://alu-intranet.hbtn.io/status')
data=()
data ["body"]= 'Body response:'
data['type'] = "- type: <class 'str'>"
data ['content'] = '- content: OK'

print (req+data.text)
