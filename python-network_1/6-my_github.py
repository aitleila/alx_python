#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
"""
import requests
import sys

def main():
    """The method used to get My GitHub username and password"""
    if len(sys.argv) != 3:
        print("Usage: python 6-my_github.py aitleila leila_dkrth0983t")
        return
    username = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/user"
    response = requests.get(url,auth=(username,token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("None")


if __name__ == "__main__":
    main()