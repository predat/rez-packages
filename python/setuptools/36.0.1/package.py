# -*- coding: utf-8 -*-

name = 'setuptools'

version = '36.0.1'

tools = ['easy_install']

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.setuptools'
