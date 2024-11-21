#!/usr/bin/python3
"""
A script that sends a request to a URL and displays the value of the
X-Request-Id variable found in the response header.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)