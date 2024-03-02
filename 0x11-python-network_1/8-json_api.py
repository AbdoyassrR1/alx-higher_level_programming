#!/usr/bin/python3
"""

"""

import requests
import sys

if __name__ == "__main__":

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    request = requests.post(url, data={"q": q})
    try:
        response = request.json()
        if response:
            print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
