<!-- Auto-generated content start -->
# pinnacle_pillow

SuperDuper Pillow is a plugin for SuperDuper that provides support for Pillow.

## Installation

```bash
pip install pinnacle_pillow
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/pillow)
- [API-docs](/docs/api/plugins/pinnacle_pillow)

| Class | Description |
|---|---|



<!-- Auto-generated content end -->

<!-- Add your additional content below -->

## Examples

We can use the `pil_image` field type to store images in a database.

```python
from pinnacle import pinnacle
from pinnacle import Table, Schema
from pinnacle_pillow import pil_image
from PIL import Image

table = Table("image", schema=Schema(identifier="image", fields={"img": pil_image}))
db = pinnacle('mongomock://test')
db.apply(table)

# Inserting an image
db["image"].insert([{"img": Image.open("test/material/data/1x1.png")}]).execute()

# Selecting an image
list(db["image"].select().execute())
```


