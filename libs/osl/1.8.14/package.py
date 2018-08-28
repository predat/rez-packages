# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "osl"

version = "1.8.14"

authors = []

description = ''

requires = [
    'openexr-2.2',
    'oiio-1.8',
    'boost-1.61'
]

build_requires = [
    'llvm-3.9',
    'cmake-3',
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.osl"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
