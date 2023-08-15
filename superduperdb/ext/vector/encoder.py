from pinnacledb.container.encoder import Encoder
from pinnacledb.ext.utils import str_shape


def vector(shape):
    return Encoder(
        identifier=f'vector[{str_shape(shape)}]',
        shape=shape,
        encoder=None,
        decoder=None,
    )
