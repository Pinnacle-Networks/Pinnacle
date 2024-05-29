**`pinnacledb.base.datalayer`** 

[Source code](https://github.com/SuperDuperDB/pinnacledb/blob/main/pinnacledb/base/datalayer.py)

## `Datalayer` 

```python
Datalayer(self,
     databackend: pinnacledb.backends.base.data_backend.BaseDataBackend,
     metadata: pinnacledb.backends.base.metadata.MetaDataStore,
     artifact_store: pinnacledb.backends.base.artifacts.ArtifactStore,
     compute: pinnacledb.backends.base.compute.ComputeBackend = <pinnacledb.backends.local.compute.LocalComputeBackend object at 0x291ee3510>)
```
| Parameter | Description |
|-----------|-------------|
| databackend | Object containing connection to Datastore. |
| metadata | Object containing connection to Metadatastore. |
| artifact_store | Object containing connection to Artifactstore. |
| compute | Object containing connection to ComputeBackend. |

Base database connector for SuperDuperDB.

## `LoadDict` 

```python
LoadDict(self,
     database: pinnacledb.base.datalayer.Datalayer,
     field: Optional[str] = None,
     callable: Optional[Callable] = None) -> None
```
| Parameter | Description |
|-----------|-------------|
| database | Instance of Datalayer. |
| field | (optional) Component type identifier. |
| callable | (optional) Callable function on key. |

Helper class to load component identifiers with on-demand loading from the database.

