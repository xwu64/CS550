import couchdb
from datetime import datetime


NUM = 10000

couch = couchdb.Server()
db = couch['paDB']

t1 = datetime.now()
for each in db:
    db.delete(each)

t2 = datetime.now()
print t2 - t1

