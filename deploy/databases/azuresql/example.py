from pinnacle import pinnacle

user = 'sa'
password = 'Pinnacle#1'
port = 1433
host = 'localhost'

db = pinnacle(f"mssql://{user}:{password}@{host}:{port}")
