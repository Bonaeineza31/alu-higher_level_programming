#!/usr/bin/python3
"""
Write script that takes in a URL,sends a request to URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
