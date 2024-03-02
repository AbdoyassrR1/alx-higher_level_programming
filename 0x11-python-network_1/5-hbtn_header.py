#!/usr/bin/python3
"""
response header value
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    print(request.headers.get("X-Request-Id"))
