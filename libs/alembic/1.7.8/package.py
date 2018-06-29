# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "alembic"

version = "1.7.8"

authors = []

description = \
    """
    """

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_requires = [
]

requires = [
    'hdf5-1.10',
    'boost-1.61',
    'openexr-2.2'
]

tools = []

uuid = "repository.alembic"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/Alembic/")
