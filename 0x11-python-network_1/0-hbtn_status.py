#!/usr/bin/python3
"""
fetch status module
"""

from urllib import request

if __name__ == "__main__":
    
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        head = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(head)))
        print("\t- content: {}".format(head))
        print("\t- utf8 content: {}".format(head.decode('utf8')))
