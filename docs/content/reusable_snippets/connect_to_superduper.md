---
sidebar_label: Connect to pinnacle
filename: connect_to_pinnacle.md
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import DownloadButton from '../downloadButton.js';


<!-- TABS -->
# Connect to pinnacle

:::note
Note that this is only relevant if you are running pinnacle in development mode.
Otherwise refer to "Configuring your production system".
:::


<Tabs>
    <TabItem value="MongoDB" label="MongoDB" default>
        ```python
        from pinnacle import pinnacle
        
        db = pinnacle('mongodb://localhost:27017/documents')        
        ```
    </TabItem>
    <TabItem value="SQLite" label="SQLite" default>
        ```python
        from pinnacle import pinnacle
        db = pinnacle('sqlite://my_db.db')        
        ```
    </TabItem>
    <TabItem value="MySQL" label="MySQL" default>
        ```python
        from pinnacle import pinnacle
        
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
        from pinnacle import pinnacle
        
        user = 'sa'
        password = 'Pinnacle#1'
        port = 1433
        host = 'localhost'
        
        db = pinnacle(f"mssql://{user}:{password}@{host}:{port}")        
        ```
    </TabItem>
    <TabItem value="PostgreSQL" label="PostgreSQL" default>
        ```python
        !pip install psycopg2
        from pinnacle import pinnacle
        
        user = 'postgres'
        password = 'postgres'
        port = 5432
        host = 'localhost'
        database = 'test_db'
        db_uri = f"postgres://{user}:{password}@{host}:{port}/{database}"
        
        db = pinnacle(db_uri, metadata_store=db_uri.replace('postgres://', 'postgresql://'))        
        ```
    </TabItem>
    <TabItem value="Snowflake" label="Snowflake" default>
        ```python
        from pinnacle import pinnacle
        
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
        from pinnacle import pinnacle
        
        user = 'default'
        password = ''
        port = 8123
        host = 'localhost'
        
        db = pinnacle(f"clickhouse://{user}:{password}@{host}:{port}", metadata_store=f'mongomock://meta')        
        ```
    </TabItem>
    <TabItem value="DuckDB" label="DuckDB" default>
        ```python
        from pinnacle import pinnacle
        
        db = pinnacle('duckdb://mydb.duckdb')        
        ```
    </TabItem>
    <TabItem value="Pandas" label="Pandas" default>
        ```python
        from pinnacle import pinnacle
        
        db = pinnacle(['my.csv'], metadata_store=f'mongomock://meta')        
        ```
    </TabItem>
    <TabItem value="MongoMock" label="MongoMock" default>
        ```python
        from pinnacle import pinnacle
        
        db = pinnacle('mongomock:///test_db')        
        ```
    </TabItem>
</Tabs>
<DownloadButton filename="connect_to_pinnacle.md" />
