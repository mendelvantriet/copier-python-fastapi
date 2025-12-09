import logging
import os
import sys


LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(LOGLEVEL)
logger.addHandler(stream_handler)
