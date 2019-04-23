# -*- coding: utf-8 -*-

name = 'pyYaml'

version = '3.12'

tools = ['']

build_requires = ["setuptools", "cython"]
requires = ["python-2.7", "libYaml"]

variants = [["platform-linux", "arch-x86_64"]]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.pyYaml'
