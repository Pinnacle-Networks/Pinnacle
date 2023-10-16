# Ask the docs anything about SuperDuperDB

In this notebook we show you how to implement the much-loved document Q&A task, using SuperDuperDB
together with MongoDB.


```python
!pip install pinnacledb
```


```python
import os

if 'OPENAI_API_KEY' not in os.environ:
    raise Exception('Environment variable "OPENAI_API_KEY" not set')
```


```python
import os
from pinnacledb import pinnacle
from pinnacledb.db.mongodb.query import Collection

# Uncomment one of the following lines to use a bespoke MongoDB deployment
# For testing the default connection is to mongomock

mongodb_uri = os.getenv("MONGODB_URI","mongomock://test")
# mongodb_uri = "mongodb://localhost:27017"
# mongodb_uri = "mongodb://pinnacle:pinnacle@mongodb:27017/documents"
# mongodb_uri = "mongodb://<user>:<pass>@<mongo_cluster>/<database>"
# mongodb_uri = "mongodb+srv://<username>:<password>@<atlas_cluster>/<database>"

# Super-Duper your Database!
from pinnacledb import pinnacle
db = pinnacle(mongodb_uri)

collection = Collection('questiondocs')
```

In this example we use the internal textual data from the `pinnacledb` project's API documentation, with the "meta"-goal of 
creating a chat-bot to tell us about the project which we are using!

Uncomment the following cell if you have the pinnacledb docs locally.
Otherwise you can load the data in the following cells.


```python
# import glob

# ROOT = '../docs/content/docs'

# STRIDE = 5       # stride in numbers of lines
# WINDOW = 10       # length of window in numbers of lines

# content = sum([open(file).readlines() 
#                for file in glob.glob(f'{ROOT}/*/*.md') 
#                + glob.glob('{ROOT}/*.md')], [])
# chunks = ['\n'.join(content[i: i + WINDOW]) for i in range(0, len(content), STRIDE)]
```


```python
!curl -O https://pinnacledb-public.s3.eu-west-1.amazonaws.com/pinnacledb_docs.json
```


```python
import json

with open('pinnacledb_docs.json') as f:
    chunks = json.load(f)
```

You can see that the chunks of text contain bits of code, and explanations, 
which can become useful in building a document Q&A chatbot.


```python
from IPython.display import Markdown
Markdown(chunks[1])
```

As usual we insert the data:


```python
from pinnacledb.container.document import Document

db.execute(collection.insert_many([Document({'txt': chunk}) for chunk in chunks]))
```

We set up a standard `pinnacledb` vector-search index using `openai` (although there are many options
here: `torch`, `sentence_transformers`, `transformers`, ...)


```python
from pinnacledb.container.vector_index import VectorIndex
from pinnacledb.container.listener import Listener
from pinnacledb.ext.openai.model import OpenAIEmbedding

db.add(
    VectorIndex(
        identifier='my-index',
        indexing_listener=Listener(
            model=OpenAIEmbedding(model='text-embedding-ada-002'),
            key='txt',
            select=collection.find(),
        ),
    )
)
```

Now we create a chat-completion component, and add this to the system:


```python
from pinnacledb.ext.openai.model import OpenAIChatCompletion

chat = OpenAIChatCompletion(
    model='gpt-3.5-turbo',
    prompt=(
        'Use the following description and code-snippets aboout SuperDuperDB to answer this question about SuperDuperDB\n'
        'Do not use any other information you might have learned about other python packages\n'
        'Only base your answer on the code-snippets retrieved\n'
        '{context}\n\n'
        'Here\'s the question:\n'
    ),
)

db.add(chat)
```

We can view that this is now registed in the system:


```python
print(db.show('model'))
```

Finally, asking questions about the documents can be targeted with a particular query.
Using the power of MongoDB, this allows users to use vector-search in combination with
important filtering rules:


```python
from pinnacledb.container.document import Document
from IPython.display import display, Markdown

q = 'Can you give me a code-snippet to set up a `VectorIndex`?'

output, context = db.predict(
    model_name='gpt-3.5-turbo',
    input=q,
    context_select=(
        collection
            .like(Document({'txt': q}), vector_index='my-index', n=5)
            .find()
    ),
    context_key='txt',
)

Markdown(output.content)
```
