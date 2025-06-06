import PIL.Image
from pinnacle.base.document import Document
from pinnacle.base.query import Query

from pinnacle_pillow import pil_image


def test_serialize_with_image():
    img = PIL.Image.open("test/material/data/test.png")
    img = img.resize((2, 2))

    r = Document({"img": pil_image(img)})

    q = Query(table="test_coll").like(r).find()
    print(q)

    s = q.encode()

    import pprint

    pprint.pprint(s)

    decode_q = Document.decode(s).unpack()

    print(decode_q)
