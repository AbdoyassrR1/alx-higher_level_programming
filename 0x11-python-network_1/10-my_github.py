#!/usr/bin/pytho3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    base = HTTPBasicAuth(username=sys.argv[1], password=sys.argv[2])
    r = requests.get(url, auth=base)

    response = r.json()
    user_id = response.get("id")
    print(user_id)
