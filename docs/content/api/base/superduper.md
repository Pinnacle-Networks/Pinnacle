**`pinnacledb.base.pinnacle`** 

[Source code](https://github.com/SuperDuperDB/pinnacledb/blob/main/pinnacledb/base/pinnacle.py)

## `pinnacle` 

```python
pinnacle(item: Optional[Any] = None,
     **kwargs) -> Any
```
| Parameter | Description |
|-----------|-------------|
| item | A database or model |
| kwargs | Additional keyword arguments to pass to the component |

Pinnacle API to automatically wrap an object to a db or a component.

Attempts to automatically wrap an item in a pinnacledb component by
using duck typing to recognize it.

