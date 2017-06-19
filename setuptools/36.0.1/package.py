# -*- coding: utf-8 -*-

name = 'setuptools'

version = '36.0.1'

tools = [
    'easy_install'
]

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7", "os-CentOS-6.8"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.setuptools'
