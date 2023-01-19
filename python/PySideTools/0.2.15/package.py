# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building

name = "PySideTools"

version = "0.2.15"

authors = [
    "pyside"
]

description = \
    """
    PySide development tools (pyuic and pyrcc)
    """

requires = [
    "shiboken-1.2",
    "PySide-1.2"
]

tools = [
    "pyside-uic",
    "pyside-rcc"
]

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

uuid = "repository.PySideTools"


def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
