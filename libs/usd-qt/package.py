# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "usdQt"

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
    # 'maya',
    # 'openexr',
    # 'glew',
    'boost',
    'tbb'
]

requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

tools = [
]

uuid = "repository.usdQt"


def commands():
    env.PYTHONPATH.append("{root}/lib/python")
