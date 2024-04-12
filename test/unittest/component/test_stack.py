from pinnacledb import pinnacle
from pinnacledb.base.document import _build_leaves
from pinnacledb.components.stack import Stack

db = pinnacle('mongomock://localhost:27017/test_db')

defn = {
    "identifier": "mystack",
    "_leaves": [
        {
            "leaf_type": "component",
            "cls": "image_type",
            "module": "pinnacledb.ext.pillow.encoder",
            "dict": {
                "identifier": "my_image",
                "media_type": "image/png"
            }
        }
    ]
}

out, exit = _build_leaves(defn["_leaves"], db)

out2 = Stack.from_list(
    content=defn["_leaves"],
    identifier=defn["identifier"],
    db=db,
)