# -*- coding: utf-8 -*-

import os

name = 'pika'

version = '0.13.1'

tools = ['']

build_requires = ["setuptools"]
requires = ["python-2.7"]

variants = [["platform-linux", "arch-x86_64"]]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.pika'
