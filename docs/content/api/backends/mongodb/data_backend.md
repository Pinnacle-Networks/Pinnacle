**`pinnacle.backends.mongodb.data_backend`** 

[Source code](https://github.com/pinnacle/pinnacle/blob/main/pinnacle/backends/mongodb/data_backend.py)

## `MongoDataBackend` 

```python
MongoDataBackend(self,
     conn: pymongo.mongo_client.MongoClient,
     name: str)
```
| Parameter | Description |
|-----------|-------------|
| conn | MongoDB client connection |
| name | Name of database to host filesystem |

Data backend for MongoDB.

