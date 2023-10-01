# A walkthrough of vector-search on MongoDB Atlas with SuperDuperDB

*In this tutorial we show developers how to execute searches leveraging MongoDB Atlas vector-search
via SuperDuperDB*

## Step 1: install `pinnacledb` Python package

```
pip install pinnacledb
```

## Step 2: connect to your Atlas cluster using SuperDuperDB

```python
import pymongo
from pinnacledb import pinnacle

URI = 'mongodb://<your-connection-string-here>'

db = pymongo.MongoClient(URI).my_database

db = pinnacle(db)
```

## Step 1: insert some data into your Atlas cluster

```python
from pinnacledb.db.mongodb.query import Collection

collection = Collection('documents')

db.execute(
    collection.insert_many([
        Document(r) for r in data
    ])
)
```