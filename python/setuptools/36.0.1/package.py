# -*- coding: utf-8 -*-

name = 'setuptools'

version = '36.0.1'

tools = ['easy_install']

requires = ["python-2.7"]

variants = [
    ["platform-linux", "arch-x86_64"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.setuptools'
