**`pinnacledb.base.leaf`** 

[Source code](https://github.com/SuperDuperDB/pinnacledb/blob/main/pinnacledb/base/leaf.py)

## `find_leaf_cls` 

```python
find_leaf_cls(full_import_path) -> Type[pinnacledb.base.leaf.Leaf]
```
| Parameter | Description |
|-----------|-------------|
| full_import_path | Full import path of the class. |

Find leaf class by class full import path.

## `Leaf` 

```python
Leaf(self,
     identifier: str,
     db: dataclasses.InitVar[typing.Optional[ForwardRef('Datalayer')]] = None,
     uuid: str = <factory>) -> None
```
| Parameter | Description |
|-----------|-------------|
| identifier | Identifier of the leaf. |
| db | Datalayer instance. |
| uuid | UUID of the leaf. |

Base class for all leaf classes.

