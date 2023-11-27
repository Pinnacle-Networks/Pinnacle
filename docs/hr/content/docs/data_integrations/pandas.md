# Pandas

Although `pandas` is not a database, it came come in very handy for testing.
To connect, one specifies a list of `.csv` files:

```python
import glob
from pinnacledb import pinnacle

db = pinnacle(glob.glob('*.csv'))
```