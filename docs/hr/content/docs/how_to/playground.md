# How to connect to and query SuperDuperDB

Now lets quickly connect to MongoDB and make it ***super-duper***!!!


```python
import pymongo

from pinnacledb import pinnacle
from pinnacledb.db.mongodb.query import Collection

db = pymongo.MongoClient().documents
db = pinnacle(db)
```


```python
db.execute(Collection('coco').find_one())
```
