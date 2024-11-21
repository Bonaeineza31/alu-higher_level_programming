#!/usr/bin/python3
"""
A script that fetches https://alu-intranet.hbtn.io/status using urllib.
The script displays
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Using a with statement to manage the request
    with urllib.request.urlopen(url) as response:
        body = response.read()

        # Displaying the required information
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))