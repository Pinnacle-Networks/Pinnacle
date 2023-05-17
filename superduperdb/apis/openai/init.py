import os

from pinnacledb.apis import api_cf
from pinnacledb.misc.logger import logging


def init_fn():
    logging.info('Setting OpenAI api-key...')
    os.environ['OPENAI_API_KEY'] = api_cf['providers']['openai']['api_key']
