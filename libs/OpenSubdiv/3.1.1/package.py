# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "opensubdiv"

version = "3.1.1"

authors = [
]

description = \
    """
    """

requires = []

build_requires = [
    'openexr-2',
    'hdf5',
    'glew',
    'tbb',
    'ptex'
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

tools = [
]

uuid = "repository.opensubdiv"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
