import couchdb
from datetime import datetime


NUM = 10000

couch = couchdb.Server()
db = couch.create('paDB')

t1 = datetime.now()
for each in range(NUM):
    key = str(each).zfill(10)
    value = str(each).zfill(90)
    pair = {'key': key, 'value': value}
    db.save(pair)

t2 = datetime.now()
print t2 - t1

