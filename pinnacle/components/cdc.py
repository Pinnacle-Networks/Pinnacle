import typing as t

from pinnacle import Component
from pinnacle.backends.base.query import Query

if t.TYPE_CHECKING:
    from pinnacle.base.datalayer import Datalayer


class CDC(Component):
    """Trigger a function when a condition is met.

    ***Note that this feature deploys on pinnacle.io Enterprise.***

    :param cdc_table: Table which fires the triggers.
    """

    triggers: t.ClassVar[t.Set] = set()
    type_id: t.ClassVar[str] = 'cdc'
    cdc_table: str 

    def __post_init__(self, db, artifacts):
        super().__post_init__(db, artifacts)

    def declare_component(self, cluster):
        super().declare_component(cluster)
        self.db.cluster.queue.put(self)
        self.db.cluster.cdc.put(self)