# MongoDB Atlas vector-search with SuperDuperDB


```python
!pip install pinnacledb==0.0.12
!pip install sentence_transformers
```

Set your `openai` key if it's not already in your `.env` variables


```python
import os
os.environ['OPENAI_API_KEY'] = '<YOUR-OPENAI-KEY>'
```

This line allows `pinnacledb` to connect to MongoDB. Under the hood, `pinnacledb` sets up configurations
for where to store:
- models
- outputs
- metadata
In addition `pinnacledb` configures how vector-search is to be performed.


```python
import os

# Uncomment one of the following lines to use a bespoke MongoDB deployment
# For testing the default connection is to mongomock

mongodb_uri = os.getenv("MONGODB_URI", "mongomock://test")
# mongodb_uri = "mongodb://localhost:27017"
# mongodb_uri = "mongodb://pinnacle:pinnacle@mongodb:27017/documents"
# mongodb_uri = "mongodb://<user>:<pass>@<mongo_cluster>/<database>"
# mongodb_uri = "mongodb+srv://<username>:<password>@<atlas_cluster>/<database>"

# Super-Duper your Database!
from pinnacledb import pinnacle
db = pinnacle(mongodb_uri)
```


```python
db
```

We've prepared some data - it's the inline documentation of the `pymongo` API!


```python
!curl -O https://pinnacledb-public.s3.eu-west-1.amazonaws.com/pymongo.json
```

We can insert this data to MongoDB using the `pinnacledb` API, which supports `pymongo` commands.


```python
import json
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.container.document import Document as D

with open('pymongo.json') as f:
    data = json.load(f)
```


```python
data[0]
```


```python
db.execute(
    Collection('documents').insert_many([D(r) for r in data])
)
```

In the remainder of the notebook you can choose between using `openai` or `sentence_transformers` to 
perform vector-search. After instantiating the model wrappers, the rest of the notebook is identical.


```python
from pinnacledb.ext.openai.model import OpenAIEmbedding

model = OpenAIEmbedding(model='text-embedding-ada-002')
```


```python
import sentence_transformers
from pinnacledb.container.model import Model
from pinnacledb.ext.vector.encoder import vector

model = Model(
    identifier='all-MiniLM-L6-v2',
    object=sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2'),
    encoder=vector(shape=(384,)),
    predict_method='encode',
    postprocess=lambda x: list(x),
    batch_predict=True,
)
```


```python
model.predict('This is a test', one=True)
```

Now we can configure the Atlas vector-search index. 
This command saves and sets up a model to "listen" to a particular subfield (or whole document) for
new text, and convert this on the fly to vectors which are then indexed by Atlas vector-search.


```python
from pinnacledb.container.vector_index import VectorIndex
from pinnacledb.container.listener import Listener

db.add(
    VectorIndex(
        identifier='pymongo-docs',
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
db.show('vector_index')
```

Now the index is set up we can use it in a query. `pinnacledb` provides some syntactic sugar for 
the `aggregate` search pipelines, which can trip developers up. It also handles 
all conversion of inputs to vectors under the hood


```python
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.container.document import Document as D
from IPython.display import *

query = 'Query the database'

result = db.execute(
    Collection('documents')
        .like(D({'value': query}), vector_index='pymongo-docs', n=5)
        .find()
)

display(Markdown('---'))

for r in result:
    display(Markdown(f'### `{r["parent"] + "." if r["parent"] else ""}{r["res"]}`'))
    display(Markdown(r['value']))
    display(Markdown('---'))
```
