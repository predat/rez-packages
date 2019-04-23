# -*- coding: utf-8 -*-

import os

name = 'numpy'

version = '1.16.3'

tools = ['f2py']

build_requires = ["setuptools", "cython"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"],
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.numpy'
