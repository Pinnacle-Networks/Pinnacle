import ibis

user = 'pinnacle'
password = 'pinnacle'
port = 1521
host = 'localhost'
database = 'test_db'

# OK
con = ibis.oracle.connect(
    user = 'pinnacle',
    password = 'pinnacle',
    port = 1521,
    host = 'localhost',
    database = 'test_db',
)

# ERROR AttributeError: 'str' object has no attribute 'username'
#con = ibis.connect(f"oracle://{user}:{password}@{host}:{port}/{database}")

# ERROR ModuleNotFoundError: No module named 'ibis.backends.base'
# from pinnacle import pinnacle
#db = pinnacle(f"oracle://{user}:{password}@{host}:{port}/{database}")