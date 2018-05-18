# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'pip'

version = '10.0.1'

tools = [
    'pip',
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

requires = [
    'setuptools',
    'python-2.7'
]

build_requires = []

uuid = 'repository.pip'


def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
