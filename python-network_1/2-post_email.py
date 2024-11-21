#!/usr/bin/python3
"""
A script that sends a POST request with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)