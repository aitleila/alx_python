#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST 
request to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""
import requests
import sys

def main():
    """The method used to search API"""
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q' : q}
    response = requests.post(url, data=payload)

    try :
        data = response.json()
        if data:
            print("[{}] {}".format (data.get('id'), data.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')

if __name__ == "__main__":
    main()