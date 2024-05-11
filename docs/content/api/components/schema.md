**`pinnacledb.components.schema`** 

[Source code](https://github.com/SuperDuperDB/pinnacledb/blob/main/pinnacledb/components/schema.py)

## `get_schema` 

```python
get_schema(db,
     schema: Union[pinnacledb.components.schema.Schema,
     str]) -> Optional[pinnacledb.components.schema.Schema]
```
| Parameter | Description |
|-----------|-------------|
| db | Datalayer instance. |
| schema | Schema to get. If a string, it will be loaded from the database. |

Handle schema caching and loading.

## `Schema` 

```python
Schema(self,
     identifier: str,
     db: dataclasses.InitVar[typing.Optional[ForwardRef('Datalayer')]] = None,
     uuid: str = <factory>,
     *,
     artifacts: 'dc.InitVar[t.Optional[t.Dict]]' = None,
     fields: Mapping[str,
     pinnacledb.components.datatype.DataType]) -> None
```
| Parameter | Description |
|-----------|-------------|
| identifier | Identifier of the leaf. |
| db | Datalayer instance. |
| uuid | UUID of the leaf. |
| artifacts | A dictionary of artifacts paths and `DataType` objects |
| fields | A mapping of field names to types or `Encoders` |

A component carrying the `DataType` of columns.

