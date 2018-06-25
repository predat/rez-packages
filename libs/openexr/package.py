# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "openexr"

version = "2.2.0"

description = \
    """
    OpenEXR
    """

build_requires = [
    'boost-1',
    'cmake',
]

requires = [
    'boost-1',
    'python-2.7',
    'numpy'
]

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.openexr"


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.append("{root}/lib64/python2.7/site-packages")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
