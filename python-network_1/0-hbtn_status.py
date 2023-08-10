"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
req = requests.get('https://alu-intranet.hbtn.io/status')

data = ()
data ["body"]= 'Body response:'
data['type'] = "- type: <class 'str'>"
data ['content'] = '- content: OK'
full_data = data['body']+data['type']+data['content']

print (req.text, "{}" "{}" "{}".format(data["body"], data["type"], data["content"]))
