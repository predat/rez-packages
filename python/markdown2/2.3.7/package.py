# -*- coding: utf-8 -*-

import os

name = 'markdown2'

version = '2.3.7'

tools = ['']

build_requires = ["setuptools"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"],
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.markdown2'
