from pinnacledb.datalayer.mongodb.data_backend import MongoDataBackend


def duck_type_mongodb(item):
    return hasattr(item, 'list_collection_names')


def duck_type_sklearn(item):
    tests = [
        hasattr(item, '_predict'),
        hasattr(item, 'fit'),
        hasattr(item, 'transform'),
        hasattr(item, 'score'),
    ]
    return sum(tests) >= 2


def duck_type_torch(item):
    tests = [
        hasattr(item, 'forward'),
        hasattr(item, 'state_dict'),
        hasattr(item, 'parameters'),
    ]
    return sum(tests) >= 3


def auto_identify(instance):
    return instance.__class__.__name__.lower()


def pinnacle(item, **kwargs):
    if duck_type_mongodb(item):
        from pymongo.database import Database

        assert isinstance(item, Database)
        from pinnacledb.datalayer.base.database import BaseDatabase
        from pinnacledb.datalayer.mongodb.metadata import MongoMetaDataStore
        from pinnacledb.datalayer.mongodb.artifacts import MongoArtifactStore

        return BaseDatabase(
            databackend=MongoDataBackend(conn=item.client, name=item.name),
            metadata=MongoMetaDataStore(conn=item.client, name=item.name),
            artifact_store=MongoArtifactStore(
                conn=item.client, name=f'_filesystem:{item.name}'
            ),
        )
    elif duck_type_sklearn(item):
        from sklearn.pipeline import Pipeline as BasePipeline
        from sklearn.base import BaseEstimator

        assert isinstance(item, BaseEstimator)
        identifier = auto_identify(item)

        if isinstance(item, BasePipeline):
            from pinnacledb.models.sklearn.wrapper import Pipeline

            return Pipeline(
                identifier=identifier, steps=item.steps, memory=item.memory, **kwargs
            )

        from pinnacledb.models.sklearn.wrapper import Estimator

        return Estimator(estimator=item, identifier=identifier, **kwargs)

    elif duck_type_torch(item):
        from torch import nn, jit

        assert isinstance(item, nn.Module) or isinstance(item, jit.ScriptModule)
        from pinnacledb.models.torch.wrapper import TorchModel

        identifier = auto_identify(item)

        return TorchModel(identifier=identifier, object=item, **kwargs)

    else:
        raise NotImplementedError(
            f'Couldn\'t auto-identify {item}, please wrap explicitly using '
            '``pinnacledb.core.*``'
        )
