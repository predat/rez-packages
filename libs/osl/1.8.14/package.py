# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "osl"

version = "1.8.14"

authors = []

description = ''

requires = ['openexr']

build_requires = [
    'llvm-3',
    'cmake',
    'openexr',
    'oiio'
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.osl"


def commands():
    env.PATH.append("{root}/bin")
