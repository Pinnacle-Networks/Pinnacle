from pinnacledb.core.metric import Metric
from pinnacledb.core.model import Model
from pinnacledb.core.model import _TrainingConfiguration
from pinnacledb.core.encoder import Encoder
from pinnacledb.core.vector_index import VectorIndex
from pinnacledb.core.watcher import Watcher

components = {
    'watcher': Watcher,
    'model': Model,
    'metric': Metric,
    'training_configuration': _TrainingConfiguration,
    'type': Encoder,
    'vector_index': VectorIndex,
}
