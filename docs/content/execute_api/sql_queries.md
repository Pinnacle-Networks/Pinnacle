# SQL select queries

In order to support as many data-backends as possible, pinnacle supports the `ibis` query API to build SQL queries.

With `pinnacle` one would write:

```python
t = db['my_table']
result = t.filter(t.brand == 'Nike').execute()
```
