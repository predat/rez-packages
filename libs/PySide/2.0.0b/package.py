# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "PySide2"

version = "2.0.0"

authors = [
    ""
]

description = \
    """
    The PySide project provides LGPL-licensed Python bindings for the Qt.
    """

requires = [
    "qt-5.6.1-adsk",
    "python-2.7"
]

build_requires = [
    'cmake-3',
    'setuptools',

    'pip'  # for sphinx, strange isn't it ?
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = []

uuid = "repository.PySide2"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
