from pinnacledb import pinnacle

user = 'default'
password = ''
port = 8123
host = 'localhost'

db = pinnacle(f"clickhouse://{user}:{password}@{host}:{port}", metadata_store=f'mongomock://meta')