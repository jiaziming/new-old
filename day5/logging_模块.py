#!/usr/bin/python
# -*-coding:utf-8-*-


import logging


logging.basicConfig(filename='example.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%Y-%m-%d-%H:%M:%S')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

'''

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
'''