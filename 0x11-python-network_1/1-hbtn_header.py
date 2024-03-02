#!/usr/bin/python3
"""
response header value
"""
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
