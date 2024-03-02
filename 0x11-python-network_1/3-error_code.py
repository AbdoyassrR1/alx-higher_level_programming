#!/usr/bin/python3
"""
error code urllib
"""


import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
