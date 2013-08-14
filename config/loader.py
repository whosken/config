#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import os.path
import yaml

default = 'config.yaml'
def load(path=None):
    if not path:
        filename = os.environ.get('CONFIG') or default
    path = path or os.path.join('config',filename)
    logging.debug('Reading yaml from <{0}>'.format(path))
    with open(path) as file:
        return yaml.load(file.read())
