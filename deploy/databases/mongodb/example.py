from pinnacledb import pinnacle

user = 'pinnacle'
password = 'pinnacle'
port = 27017
host = 'localhost'
database = 'test_db'

db = pinnacle(f"mongodb://{user}:{password}@{host}:{port}/{database}")