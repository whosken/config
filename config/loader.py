#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os.path
import yaml

default = 'config.yaml'
def load(path=None):
    path = path or os.path.join('config',default)
    logging.debug('Reading yaml from <{0}>'.format(path))
    with open(path) as file:
        raw_yaml = file.read()
    return yaml.load(raw_yaml)
