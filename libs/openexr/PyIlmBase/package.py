# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "PyIlmBase"

version = "2.2.0"

description = \
    """
    """

build_requires = [
    #'cmake-3',
]

requires = [
    'openexr-2.2',
    'boost-1.61',
    'numpy'
]

variants = [["platform-linux", "arch-x86_64", "python-2.7"]]

uuid = "repository.PyIlmBase"


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.append("{root}/lib64/python2.7/site-packages")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
