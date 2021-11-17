from github import Github
import json
import pymongo
print("hello test")
g = Github("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")
user = g.get_user()
print("user: " + user.login)
# if user.name is not None:
#     print("fullname: " + user.name)
# if user.location is not None:
#     print("location: " + user.location)
# if user.company is not None:
#     print("company: " + user.company)
dct = {'user': user.login,
    'fullname': user.name,
    'location': user.location,
    'company': user.company}
print("dictionary is " + json.dumps(dct))

# now let's store the dictionary in a mongodb

# first we need to remove null fields from the dictionary, because
# if we don't we'll end up with null fields in the db. This will cause us
# lots of debugging problems later. The convention is only store actual data
# in the database.

for k, v in dict(dct).items():
    if v is None:
        del dct[k]

print ("cleaned dictionary is " + json.dumps(dct))

# now let's store the data.

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.insert_many([dct])