import urllib.request
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
req = urllib.request.Request('https://alu-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
   html = response.read()
