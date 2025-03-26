<!-- Auto-generated content start -->
# pinnacle_sql

pinnacle-sql is a plugin for SQL databackends that allows you to use these backends with pinnacle.


Pinnacle supports SQL databases via the ibis project. With pinnacle, queries may be built which conform to the ibis API, with additional support for complex data-types and vector-searches.


## Installation

```bash
pip install pinnacle_sql
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/ibis)
- [API-docs](/docs/api/plugins/pinnacle_ibis)

| Class | Description |
|---|---|
| `pinnacle_sql.data_backend.SQLDataBackend` | sql data backend for the database. |


<!-- Auto-generated content end -->

<!-- Add your additional content below -->

## Connection examples

### MySQL

```python
from pinnacle import pinnacle

db = pinnacle('mysql://<mysql-uri>')
```

### Postgres

```python
from pinnacle import pinnacle

db = pinnacle('postgres://<postgres-uri>')
```

### Other databases

```python

from pinnacle import pinnacle

db = pinnacle('<database-uri>')
```