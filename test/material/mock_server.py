import random

import lorem
import PIL.Image

from pinnacledb import ObjectModel
from pinnacledb.backends.mongodb.query import MongoQuery
from pinnacledb.base.pinnacle import pinnacle
from pinnacledb.components.stack import Stack
from pinnacledb.ext.numpy import array
from pinnacledb.ext.pillow.encoder import image_type
from pinnacledb.rest.app import build_app
from pinnacledb.server.app import SuperDuperApp

m = Stack(
    'test_stack',
    components=[
        ObjectModel(
            'test',
            object=lambda x: x + 2,
            datatype=array('float32', shape=(32,)),
        ),
        ObjectModel(
            'test2',
            object=lambda x: x + 3,
            datatype=array('float32', shape=(16,)),
        ),
    ],
)

from pinnacledb.base.document import Document

collection = MongoQuery('documents')
data = [
    Document({'x': random.randrange(100), 'y': lorem.sentence()}) for _ in range(100)
]

db = pinnacle('mongomock://test')
db.execute(collection.insert_many(data))
db.add(m)

from pinnacledb.ext.openai import OpenAIChatCompletion

m = OpenAIChatCompletion(identifier='gpt-3.5-turbo')

r = m.export_to_references()

import json

str_ = json.dumps(r, indent=2).replace('"', '\"')


import os

os.system(f"echo '{str_}'")
os.system(f"echo '{str_}' | pbcopy")

img = PIL.Image.open('test/material/data/rickroll.png')

_, i = db.add(image_type('image'))
insert = MongoQuery('images').insert_one(Document({'img': i(img)}))

db.execute(insert)

app = SuperDuperApp('rest', port=8002, db=db)

build_app(app)
app.start()
