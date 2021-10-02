"""
HW04a: Developing with the Perspective of the Tester in mind
Date:10/02/2021
@author: Emay Pandarakutty
email: epandar@stevens.edu
"""
import requests
import json


def get_repos(user_id):
    """
    This function find and return the repositories name for the given user id.
    failure to get the repository/repo name  for provided user id return an exception.

    https: // api.github.com / users / < ID > / repos
    """
    repos = []
    # get the repo URl
    try:
        repo_url = requests.get('https://api.github.com/users/' + str(user_id) + '/repos')
        if repo_url.status_code != 200:# if not finding a valid url return error
            return"repo url error"
    except():
        return "Unable to get the repo url"

    repo_url_dict = json.loads(repo_url.text)
    # get the repo name
    for repo in repo_url_dict:
        try:
            repos.append(repo['name'])
        except():
            return "Repository name not valid"
    return repos


def get_commits(user_id, repo):
    """
    This function get user id and repo name as input and return total commits for reach repo.
    raise exception if any error in getting the commits
    https: // api.github.com / repos / < ID > / < REPO > / commits

    """
    # get all the commits done for passed user ip and repo name
    try:
        commit_url = requests.get('https://api.github.com/repos/' + str(user_id) + '/' + str(repo) + '/commits')
        if commit_url.status_code != 200: # if not finding a valid url return error
            return"commit url error"
    except():
        return "Unable to get the commits"

    commit_url_dict = json.loads(commit_url.text)
    total_commits = 'Repo: ' + str(repo) + '  Number of commits: ' + str(len(commit_url_dict))

    return total_commits


def main(user_id):
    for repo in get_repos(user_id):
        print(get_commits(user_id, repo))


if __name__ == '__main__':
    user_id = input("Enter github user ID: ")
    main(user_id)
