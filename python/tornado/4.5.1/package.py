# -*- coding: utf-8 -*-

import os

name = 'tornado'

version = '4.5.1'

tools = ['']

build_requires = ["setuptools"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.tornado'
