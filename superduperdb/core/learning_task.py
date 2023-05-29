from typing import List, Mapping, Union

from pinnacledb.core.base import Component, ComponentList
from pinnacledb.core.metric import Metric
from pinnacledb.core.model import Model
from pinnacledb.core.training_configuration import TrainingConfiguration
from pinnacledb.datalayer.base.query import Select


class LearningTask(Component):
    variety = 'learning_task'

    def __init__(
        self,
        identifier: str,
        models: List[Union[Model, str]],
        keys: List[str],
        select: Select,
        training_configuration: TrainingConfiguration,
        validation_sets: List[str],
        metrics: List[Metric],
        features: Mapping[str, str],
    ):
        super().__init__(identifier)
        self.models = ComponentList(models)
        self.keys = keys
        self.training_configuration = training_configuration
        self.identifier = identifier
        self.validation_sets = validation_sets
        self.metrics = metrics
        self.features = features
        self.select = select

    def schedule_jobs(self, database, verbose=True, dependencies=()):
        return [database.fit(self.identifier, verbose=verbose, dependencies=dependencies)]
