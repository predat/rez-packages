# -*- coding: utf-8 -*-

name = 'requests'

version = '2.13.0'

tools = ['']

build_requires = ["setuptools"]

requires = []

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.requests'
