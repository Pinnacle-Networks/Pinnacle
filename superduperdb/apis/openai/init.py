import os

from pinnacledb import cf
from pinnacledb.misc.logger import logging


def init_fn():
    logging.info('Setting OpenAI api-key...')
    os.environ['OPENAI_API_KEY'] = cf['apis']['providers']['openai']['api_key']
