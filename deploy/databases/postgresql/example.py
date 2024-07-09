from pinnacle import pinnacle

user = 'pinnacle'
password = 'pinnacle'
port = 5432
host = 'localhost'
database = 'test_db'
db_uri = f"postgres://{user}:{password}@{host}:{port}/{database}"

db = pinnacle(db_uri, metadata_store=db_uri.replace('postgres://', 'postgresql://')) 