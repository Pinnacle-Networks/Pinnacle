---
sidebar_position: 4
---

# Setting up Pinnacle as a change-data-capture daemon

:::info
This functionality is currently for MongoDB only
:::

Setting-up Pinnacle as a change-data-capture daemon, is a simple call:

```python
db.cdc.listen()
```

... or

```bash
pinnacle cdc
```

When `pinnacle` is configured in this way, this daemon handles all inserts to 
Pinnacle, therefore, if `pinnacle` is run in another process or service, 
it's important to configure the existence of the daemon:

```python
from pinnacle import CFG

CFG.cluster.cdc = True
```

Now that the daemon is running, even when data is inserted using a different client, such as
the native `pymongo.MongoClient` client, then `Listener` outputs are still created on those inputs.