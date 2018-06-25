# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "usd_arnold"

version = "0.0.1"

authors = [
    'LumaPictures'
]

description = \
    """
Reusable UI widgets for viewing and authoring USD files
    """

build_requires = [
    'cmake',
    'usd',
    'boost',
    'tbb',
    'arnold',
    'usd_arnold'
]

requires = [
    'mtoa',
    'maya'
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7", "maya-2018"]
]

tools = [
]

uuid = "repository.arnold"


def commands():
    env.PYTHONPATH.append("{root}/lib/python")
