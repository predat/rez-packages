# -*- coding: utf-8 -*-

import os

name = 'pika'

version = '1.0.1'

tools = ['']

build_requires = ["setuptools"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"],
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.pika'
