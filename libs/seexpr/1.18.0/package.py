# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "seexpr"

version = "1.18.0"

authors = ['']

description = \
    """
    """

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]


build_requires = [
    'python-2.7',
    'boost',
    'llvm-3',
    'qt-4',
    'pyqt4'
]

requires = [
]

tools = []

uuid = "repository.seexpr"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
