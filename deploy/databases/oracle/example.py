from pinnacledb import pinnacle

user = 'pinnacle'
password = 'pinnacle'
port = 1521
host = 'localhost'

db = pinnacle(f"oracle://{user}:{password}@{host}:{port}")