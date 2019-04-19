# -*- coding: utf-8 -*-

import os

name = 'cython'

@early()
def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

tools = ['cygdb', 'cython', 'cythonize']

build_requires = ["setuptools"]

variants = [
    ["platform-linux", "python-3"],
    ["platform-linux", "python-2.7"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.cython'
