#!/usr/bin/python3
"""
post email mudule
"""

import sys
import urllib


if __name__ == "__main__":

    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
