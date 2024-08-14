**`pinnacle.base.pinnacle`** 

[Source code](https://github.com/pinnacle/pinnacle/blob/main/pinnacle/base/pinnacle.py)

## `pinnacle` 

```python
pinnacle(item: Optional[Any] = None,
     **kwargs) -> Any
```
| Parameter | Description |
|-----------|-------------|
| item | A database or model |
| kwargs | Additional keyword arguments to pass to the component |

`pinnacle` API to automatically wrap an object to a db or a component.

Attempts to automatically wrap an item in a pinnacle.ioponent by
using duck typing to recognize it.

