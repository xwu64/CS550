from pymongo import MongoClient
from datetime import datetime


NUM = 10000

client = MongoClient()
db = client.test_database
collection = db.test_collection

t1 = datetime.now()
for each in range(NUM):
    key = str(each).zfill(10)
    value = str(each).zfill(90)
    post = {"key": key, "value": value}
    posts = db.posts
    posts.insert_one(post)

t2 = datetime.now()
print t2 - t1
