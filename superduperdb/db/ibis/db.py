import typing as t

from pinnacledb.db.ibis.cursor import SuperDuperIbisCursor
from pinnacledb.db.base.db import DB
from pinnacledb.container.component import Component
from pinnacledb.container.job import Job
from pinnacledb.db.ibis.query import OutputTable
from pinnacledb import logging


class IbisDB(DB):
    def _execute(self, query, parent):
        table = parent
        for member in query.members:
            parent = member.execute(
                self, parent, table=query.collection, ibis_table=table
            )
        cursor = SuperDuperIbisCursor(parent, query.collection.primary_id, encoders=self.encoders)
        return cursor.execute()

    def execute(self, query):
        table = query.collection.get_table(self.db)
        return self._execute(query, table)

    def add(self, 
            object: Component,
            dependencies: t.Sequence[Job] = (),
        ):
        super().add(object, dependencies=dependencies)
        try:
            table = OutputTable(model=object.identifier)
            table.create(self.db)
        except Exception as e:
            logging.error(e)
        else:
            logging.debug(f"Created output table for {object.identifier}")
