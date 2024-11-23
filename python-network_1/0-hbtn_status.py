#!/usr/bin/python3
"""A script that fetches https://alu-intranet.hbtn.io/status
with the  use of  urllib."""


import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"  # Correct URL

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))