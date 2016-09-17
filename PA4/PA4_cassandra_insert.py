from cassandra.cluster import Cluster
from datetime import datetime


OPERATION_NUM = 100000


cluster = Cluster()
session = cluster.connect('pakeyspace')

p1 = datetime.now()
for each in range(0, OPERATION_NUM/2):
    str_each = str(each)
    key = str_each.zfill(10)
    value = key*9
    session.execute(
    """
    INSERT INTO DHT (key, value)
    VALUES (%s, %s)
    """,
    (key, value)
    )

p2 = datetime.now()
print (p2 - p1)
