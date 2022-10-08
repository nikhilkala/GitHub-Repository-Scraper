from mongo_usage import *
from utils import *


def insert_public_repos(usernames):
    import requests
    from bs4 import BeautifulSoup
    import html5lib

    repo_list = []
    if isinstance(usernames, list):
        for username in usernames:
            if isinstance(username, str) and username_exists(username):
                repo_list = []
                for page in range(1, 100):
                    url = "https://github.com/" + username + "?page=" + str(page) + "&tab=repositories"
                    q = requests.get(url)
                    if q.ok:
                        soup = BeautifulSoup(q.content, 'html5lib')
                        repo_data = soup.find_all("a", itemprop="name codeRepository")
                        repo_page = [str(repo.string).replace('\n', '').strip() for repo in repo_data]
                        if not repo_page:
                            break
                        repo_list.extend(repo_page)
                    else:
                        break
            else:
                continue
            insert_repos(username, repo_list, len(repo_list))
    elif isinstance(usernames, str) and username_exists(usernames):
        repo_list = []
        for page in range(1, 100):
            url = "https://github.com/" + usernames + "?page=" + str(page) + "&tab=repositories"
            q = requests.get(url)
            if q.ok:
                soup = BeautifulSoup(q.content, 'html5lib')
                repo_data = soup.find_all("a", itemprop="name codeRepository")
                repo_page = [str(repo.string).replace('\n', '').strip() for repo in repo_data]
                if not repo_page:
                    break
                repo_list.extend(repo_page)
            else:
                break
        insert_repos(usernames, repo_list, len(repo_list))


if __name__ == '__main__':
    insert_public_repos(['snataraja'])
    user_list = ['nikhilkala', 'isha-talegaonkar', 'snataraja', 'snatarajappa', 'npurushe']
    insert_public_repos(user_list)
    input_list = []
    while True:
        username = input("Enter git username / 0 to exit")
        if username == str(0):
            break
        input_list.append(username)
    insert_public_repos(input_list)
