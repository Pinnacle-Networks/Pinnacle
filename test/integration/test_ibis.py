import ibis
import PIL.Image
import pandas
from sklearn import svm
import torchvision

from pinnacledb import pinnacle
from pinnacledb import CFG
from pinnacledb.container.encoder import Encoder
from pinnacledb.container.schema import Schema
from pinnacledb.db.base.build import build_vector_database
from pinnacledb.container.document import Document as D
from pinnacledb.db.ibis.db import IbisDB
from pinnacledb.db.filesystem.artifacts import FileSystemArtifactStore
from pinnacledb.db.ibis.data_backend import IbisDataBackend
from pinnacledb.db.sqlalchemy.metadata import SQLAlchemyMetadata
from pinnacledb.db.ibis.query import Table
from pinnacledb.ext.pillow.image import pil_image
from pinnacledb.ext.torch.model import TorchModel
# from pinnacledb.container.schema import Schema


connection = ibis.sqlite.connect("mydb.sqlite")

# Insert some sample data into the table
schema = ibis.schema({'id': 'int64', 'health': 'int32', 'age': 'int32'})
# Create the table
table_name = 'my_table'

# connection.create_table(table_name, schema=schema)


# create data layer
db = IbisDB(
    databackend=IbisDataBackend(conn=connection, name='ibis'),
    metadata=SQLAlchemyMetadata(conn=connection.con, name='ibis'),
    artifact_store=FileSystemArtifactStore(
        conn='./.tmp', name='ibis'
    ),
    vector_database=build_vector_database(CFG.vector_search.type),
)

schema = Schema(
    identifier='my_table',
    fields={
        'id': 'int64',
        'health': 'int32',
        'age': 'int32',
        'image': pil_image,
    }
)

im = PIL.Image.open('test/material/data/test-image.jpeg')

data_to_insert = [
    (1, 0, 25, im),
    (2, 1, 26, im),
    (3, 1, 27, im),
    (4, 1, 28, im),
    (5, 0, 29, im),
]

t = Table(identifier='my_table', schema=schema)

t.create(db, schema=...)

def create(self, db, schema):
    db.add(schema)
    new_schema = {}
    for k, v in schema.fields.items():
        if isinstance(v, Encoder):
            new_schema[f'{k}::_encodable={v.identifier}/{v.version}::'] = 'binary'
    self.conn.create_table(self.identifier, schema=schema.fields)

db.add(t)

db.execute(
    t.insert([D(d) for d in data_to_insert])
)

# preprocessing function
preprocess = torchvision.transforms.Compose([
    torchvision.transforms.Resize(256),
    torchvision.transforms.CenterCrop(224),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)])

# create a torchvision model
resnet = TorchModel(
    preprocess=preprocess,
    object=torchvision.models.resnet18(pretrained=True),
)

# apply the torchvision model
resnet.predict(X='image', db=db, select=t, max_chunk_size=3000, overwrite=True)

# add a sklearn model


svc = svm.SVC(gamma='scale', class_weight='balanced', C=100, verbose=True)
svc.fit(pandas.DataFrame(data_to_insert).iloc[:, :3], [0, 1, 1, 1, 0])

model = pinnacle(
    svc,
    postprocess=lambda x: int(x),
    preprocess=lambda x: list(x.values()
))

model.predict(X='_base', db=db, select=table.filter(table.age > 25), max_chunk_size=3000, overwrite=True)    

#  Query result back
out_table = connection.table(model.identifier)
q = table.filter(table.age > 26).outputs(model.identifier, db)

curr = db.execute(q)
for c in curr:
    print(c)
