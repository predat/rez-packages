# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "sip"

version = "4.19.1"

authors = ['']

description = \
    """
    """

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]


build_requires = [
]

requires = []

tools = []

uuid = "repository.sip"


def commands():
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.PATH.append("{root}/bin")
