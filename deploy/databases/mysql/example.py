from pinnacle import pinnacle

user = 'pinnacle'
password = 'pinnacle'
port = 3306
host = 'localhost'
database = 'test_db'

db = pinnacle(f"mysql://{user}:{password}@{host}:{port}/{database}")