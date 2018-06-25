# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "pyqt4"

version = "4.12.1"

authors = ['']

description = \
    """
    """

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]


build_requires = [
]

requires = [
    'python-2.7',
    'sip',
    'qt-4'
]

tools = []

uuid = "repository.sip"


def commands():
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.PATH.append("{root}/bin")
