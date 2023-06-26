from pinnacledb.core.fit import Fit
from pinnacledb.core.metric import Metric
from pinnacledb.core.model import Model
from pinnacledb.core.model import TrainingConfiguration
from pinnacledb.core.encoder import Encoder
from pinnacledb.core.vector_index import VectorIndex
from pinnacledb.core.watcher import Watcher

components = {
    'watcher': Watcher,
    'model': Model,
    'fit': Fit,
    'metric': Metric,
    'training_configuration': TrainingConfiguration,
    'type': Encoder,
    'vector_index': VectorIndex,
}
