---
sidebar_label: Connect to SuperDuperDB
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- TABS -->
# Connect to SuperDuperDB

:::note
Note that this is only relevant if you are running SuperDuperDB in development mode.
Otherwise refer to "Configuring your production system".
:::


<Tabs>
    <TabItem value="MongoDB" label="MongoDB" default>
        ```python
        from pinnacledb import pinnacle
        
        db = pinnacle('mongodb://localhost:27017/documents')        
        ```
    </TabItem>
    <TabItem value="SQLite" label="SQLite" default>
        ```python
        from pinnacledb import pinnacle
        
        db = pinnacle('sqlite://my_db.db')        
        ```
    </TabItem>
    <TabItem value="MySQL" label="MySQL" default>
        ```python
        from pinnacledb import pinnacle
        
        user = 'pinnacle'
        password = 'pinnacle'
        port = 3306
        host = 'localhost'
        database = 'test_db'
        
        db = pinnacle(f"mysql://{user}:{password}@{host}:{port}/{database}")        
        ```
    </TabItem>
    <TabItem value="Oracle" label="Oracle" default>
        ```python
        from pinnacledb import pinnacle
        
        user = 'sa'
        password = 'Pinnacle#1'
        port = 1433
        host = 'localhost'
        
        db = pinnacle(f"mssql://{user}:{password}@{host}:{port}")        
        ```
    </TabItem>
    <TabItem value="PostgreSQL" label="PostgreSQL" default>
        ```python
        from pinnacledb import pinnacle
        
        user = 'pinnacle'
        password = 'pinnacle'
        port = 5432
        host = 'localhost'
        database = 'test_db'
        
        db = pinnacle(f"postgres://{user}:{password}@{host}:{port}/{database}")        
        ```
    </TabItem>
    <TabItem value="Snowflake" label="Snowflake" default>
        ```python
        from pinnacledb import pinnacle
        
        user = "pinnacleuser"
        password = "pinnaclepassword"
        account = "XXXX-XXXX"  # ORGANIZATIONID-USERID
        database = "FREE_COMPANY_DATASET/PUBLIC"
        
        snowflake_uri = f"snowflake://{user}:{password}@{account}/{database}"
        
        db = pinnacle(
            snowflake_uri, 
            metadata_store='sqlite:///your_database_name.db',
        )        
        ```
    </TabItem>
    <TabItem value="Clickhouse" label="Clickhouse" default>
        ```python
        from pinnacledb import pinnacle
        
        user = 'default'
        password = ''
        port = 8123
        host = 'localhost'
        
        db = pinnacle(f"clickhouse://{user}:{password}@{host}:{port}", metadata_store=f'mongomock://meta')        
        ```
    </TabItem>
    <TabItem value="DuckDB" label="DuckDB" default>
        ```python
        from pinnacledb import pinnacle
        
        db = pinnacle('duckdb://mydb.duckdb')        
        ```
    </TabItem>
    <TabItem value="Pandas" label="Pandas" default>
        ```python
        from pinnacledb import pinnacle
        
        db = pinnacle(['my.csv'], metadata_store=f'mongomock://meta')        
        ```
    </TabItem>
    <TabItem value="MongoMock" label="MongoMock" default>
        ```python
        from pinnacledb import pinnacle
        
        db = pinnacle('mongomock:///test_db')        
        ```
    </TabItem>
</Tabs>
