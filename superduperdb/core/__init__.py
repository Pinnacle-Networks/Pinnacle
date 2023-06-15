from pinnacledb.core.learning_task import LearningTask
from pinnacledb.core.metric import Metric
from pinnacledb.core.model import Model
from pinnacledb.core.training_configuration import TrainingConfiguration
from pinnacledb.core.encoder import Encoder
from pinnacledb.core.vector_index import VectorIndex
from pinnacledb.core.watcher import Watcher

components = {
    'watcher': Watcher,
    'model': Model,
    'learning_task': LearningTask,
    'metric': Metric,
    'training_configuration': TrainingConfiguration,
    'type': Encoder,
    'vector_index': VectorIndex,
}
