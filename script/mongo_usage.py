import pymongo
from pymongo import MongoClient
from constants import db_client


def make_document(username, repo_list, repo_number):
    document = {"username": username, "repositories": repo_list, "repo_count": repo_number}
    return document


def make_repos_document(username, repo_list, repo_number):
    document = {"username": username, "repositories": repo_list, "repo_count": repo_number}
    return document


def make_users_document(user_list):
    document = {"users": user_list}
    return document


def get_filter(document):
    filter_query = {'$set': document}
    return filter_query


def get_query(username):
    query = {"username": username}
    return query


def get_user_query():
    query = {}
    return query


def get_collection():
    github_user_db = db_client.github
    collection = github_user_db.repositories
    return collection


def insert_repos(username, repo_list, repo_number):
    collection = get_collection()
    document = make_document(username, repo_list, repo_number)
    filter_query = get_filter(document)
    collection.update_one(filter=document, upsert=True, update=filter_query)


def get_repos(username, skip, limit):
    collection = get_collection()
    query = get_query(username)
    repos = collection.find_one(query)
    repo_list = []
    repo_count = 0
    if repos is not None:
        repo_count = repos.get('repo_count')
        if limit > 0:
            repo_list = repos.get('repositories')[skip:skip+limit]
        else:
            repo_list = repos.get('repositories')[skip:]
    return make_repos_document(username, repo_list, repo_count)


def get_users():
    collection = get_collection()
    query = get_user_query()
    users = collection.find(query)
    user_list = []
    for user in users:
        user_list.append(user.get('username'))
    return make_users_document(user_list)
