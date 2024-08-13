from pinnacle import logging


def _warn_plugin_deprecated(name):
    message = (
        f'pinnacle.ext.{name} is deprecated '
        'and will be removed in a future release.'
        f'Please insteall pinnacle_{name} and use'
        f'from pinnacle_{name} import * instead.'
    )
    logging.warn(message)
