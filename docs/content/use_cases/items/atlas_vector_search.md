# MongoDB Atlas vector-search with SuperDuperDB


```python
!pip install pinnacledb
```


```python
!curl -O https://pinnacledb-public.s3.eu-west-1.amazonaws.com/pymongo.json
```

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  120k  100  120k    0     0   387k      0 --:--:-- --:--:-- --:--:--  392k



```python
import os

os.environ['OPENAI_API_KEY'] = '<YOUR-OPEN-AI-API-KEY-HERE>'
```


```python
import pymongo
from pinnacledb import pinnacle

db = pymongo.MongoClient().pymongo_docs
    
db = pinnacle(db)
```


```python
import json
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.container.document import Document as D

with open('pymongo.json') as f:
    data = json.load(f)

db.execute(Collection('documents').insert_many([D(r) for r in data]))
```


```python
from pinnacledb.container.vector_index import VectorIndex
from pinnacledb.container.listener import Listener
from pinnacledb.ext.numpy.array import array
from pinnacledb.ext.openai.model import OpenAIEmbedding


model = OpenAIEmbedding(model='text-embedding-ada-002')

db.add(
    VectorIndex(
        identifier=f'pymongo-docs',
        indexing_listener=Listener(
            model=model,
            key='value',
            select=Collection('documents').find(),
            predict_kwargs={'max_chunk_size': 1000},
        ),
    )
)
```


```python
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.container.document import Document as D
from IPython.display import *

query = 'Find data'

result = db.execute(
    Collection('documents')
        .like(D({'value': query}), vector_index='pymongo-docs', n=5)
        .find()
)

for r in result:
    display(Markdown(f'### `{r["parent"] + "." if r["parent"] else ""}{r["res"]}`'))
    display(Markdown(r['value']))
```
