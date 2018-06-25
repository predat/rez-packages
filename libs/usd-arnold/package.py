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
    'openexr'
]

requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    'usdAiShaderInfo'
]

uuid = "repository.arnold"


def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python")
    env.PXR_PLUGINPATH.append("{root}")
