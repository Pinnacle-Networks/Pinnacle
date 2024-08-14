# SQL select queries

In order to support as many data-backends as possible, Pinnacle supports the `ibis` query API to build SQL queries.

With Pinnacle one would write:

```python
t = db['my_table']
result = t.filter(t.brand == 'Nike').execute()
```
