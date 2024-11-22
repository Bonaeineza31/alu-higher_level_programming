#!/usr/bin/python3
"""A script that fetches https://alu-intranet.hbtn.io/status
with the  use of  urllib."""


import urllib.request

url = "https://alu-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
