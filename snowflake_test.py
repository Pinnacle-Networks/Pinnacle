import json

from pinnacle_openai import OpenAIEmbedding
from pinnacle import *
from pinnacle.components.datatype import Vector

CFG.auto_schema = True
CFG.vector_search_engine = 'snowflake'
CFG.data_backend = 'snowflake://softwareuser:SU4yv6DfUPUL0CPDdsCDDSLttVc@ngkjqqn-pinnacledbeu/myuser_db/data'

m = OpenAIEmbedding(
    'test', 
    model='text-embedding-ada-002',
    example='test',
)

db = pinnacle()
db.cfg.auto_schema = True

with open('text.json') as f:
    data = json.load(f)

db['test'].insert(data).execute()

vector_index = VectorIndex(
    'test',
    indexing_listener=Listener(
        'test',
        model=m,
        select=db['test'].select(),
        key='txt'
    ),
    measure='l2'
)

db.apply(vector_index, force=True)

for r in db['test'].like({'txt': 'Axel Covin'}, n=1, vector_index='test').select().execute():
    print(r['txt'])