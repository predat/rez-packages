# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, resolve  # make linter happy


name = "pyside2"

version = "5.11.1"

authors = ['']

description = \
    """
    """

build_requires = ['llvm', 'setuptools']
requires = ['qt5']
build_command = "bash {root}/build.sh {install}"
variants = [["platform-linux", "arch-x86_64", "python-2"]]

tools = []

uuid = "repository.pyside2"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")
