# Core pinnacle usage

In this section we walk through how to perform the key operations with pinnacle.
There are three key patterns C-A-E:

***Connect***

```python
from pinnacle import pinnacle
db = pinnacle('<data-connection>')
```

***Apply***

```python
db.apply(<ai_component>)
```

***Execute***

```python
to_execute = <build_your_database_query_or_model_prediction>
db.execute(to_execute)
```
