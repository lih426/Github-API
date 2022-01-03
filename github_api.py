import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint

# personal access token
API_KEY = "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"

# github username
username = "lih426"

# pygithub object
g = Github(API_KEY)
user = g.get_user(username)

def printRepo(repo):
    print("Repo name:", repo.full_name)
    print("Time created:", repo.created_at)
    print("\nLanguage:", repo.language)
    print("Stars:", repo.stargazers_count)
    getRepoCommits(repo)
   

def getRepoCommits(repo):
    try:
        if repo.get_commits() is not None:
            commits = repo.get_commits().totalCount
            print(f"Number of commits: {commits}")
    except:
        print("Number of commits: 0")

count = 0
print("------------------------------")
for repo in user.get_repos():
    count =  count + 1
    if repo is not None:
        print("Repository No." + "{count}")
        printRepo(repo)
        print("------------------------------")