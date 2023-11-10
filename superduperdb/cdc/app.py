from pinnacledb import CFG
from pinnacledb.base.datalayer import Datalayer
from pinnacledb.components.listener import Listener
from pinnacledb.server import app as pinnacleapp

port = int(CFG.server.cdc.split(':')[-1])
app = pinnacleapp.SuperDuperApp('cdc', port=port)


@app.startup
def cdc_startup(db: Datalayer):
    db.cdc.start()


@app.add('/listener/add', method='get')
def add_listener(name: str, db: Datalayer = pinnacleapp.DatalayerDependency()):
    '''
    Endpoint for adding a listener to cdc
    '''
    listener = db.load('listener', name)
    assert isinstance(listener, Listener)
    db.cdc.add(listener)


@app.add('/listener/delete', method='get')
def remove_listener(name: str, db: Datalayer = pinnacleapp.DatalayerDependency()):
    '''
    Endpoint for removing a listener from cdc
    '''
    listener = db.load('listener', name)
    assert isinstance(listener, Listener)
    on = listener.select.table_or_collection.identifier
    db.cdc.stop(on)
