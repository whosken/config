#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import config

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
        'config',
    ]

requires = [
        'yaml'
    ]

setup(
    name='config',
    version=config.__version__,
    description='Extended YAML and Environment Variable Reader',
    long_description=open('README.md').read(),
    author='Soshio',
    author_email='tech@getsoshio.com',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'config': ['*.pem']},
    package_dir={'config': 'config'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',

    ),
)