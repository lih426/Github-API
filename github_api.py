import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint

# asks user for personal access token
api_key = input("Enter your GitHub personal access token:\n")

# init pygithub object
g = Github(api_key)

# prints all repositories of given user object
def printAllRepos(user):
    print(f"\nName of User: {user.name}")
    count = 0
    print("------------------------------")
    for repo in user.get_repos():
        count =  count + 1
        if repo is not None:
            print(f"Repository No.{count}")
            printRepo(repo)
            print("------------------------------")

# prints information of a repository
def printRepo(repo):
    print("Repo name:", repo.full_name)
    print("Time created:", repo.created_at)
    print("\nLanguage:", repo.language)
    print("Stars:", repo.stargazers_count)
    getRepoCommits(repo)
   
# prints number of commits to a repository
def getRepoCommits(repo):
    try:
        if repo.get_commits() is not None:
            commits = repo.get_commits().totalCount
            print(f"Number of commits: {commits}")
    except:
        print("Number of commits: 0")

# asks for username, prints all repositories
while True:
    username = input("Enter GitHub usrname:\n")
    user = g.get_user(username)
    printAllRepos(user)