import requests


def username_exists(username):
    url = "https://github.com/" + username
    q = requests.get(url)
    if q.ok:
        return True
    else:
        return False
