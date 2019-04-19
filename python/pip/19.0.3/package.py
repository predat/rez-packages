# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'pip'

@early()
def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

tools = [
    'pip',
]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"]
]

requires = [
    'setuptools',
]

build_requires = []

uuid = 'repository.pip'


def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
