import os

from pinnacledb import CFG
from pinnacledb.misc.logger import logging


def init_fn():
    logging.info('Setting OpenAI api-key...')
    os.environ['OPENAI_API_KEY'] = CFG.apis.providers['openai']['api_key']
