# -*- coding: utf-8 -*-

name = 'cmake'

version = '3.25.1'

authors = ["Kitware"]

description = \
"""
Cross platform build system
"""

requires = [
    #'~qt-6.4'
]

private_build_requires = [
    'gcc-9+',
    'cmake-3',
    'openssl-3<3.1',
    'zlib-1.2',
    #'qt-6.4'
]

variants = [["platform-linux"]]

uuid = "repository.cmake"

tools = [
    "cmake",
    "ccmake",
    "cpack",
    "ctest"
]

# with scope("config") as config:
#     config.release_packages_path = '/s/apps/packages/dev'


def commands():
    env.PATH.append("{root}/bin")

    source("{root}/share/bash-completion/completions/cmake")
