# -*- coding: utf-8 -*-

name = "openexr"

version = "2.4.1"

description = \
"""
OpenEXR
"""

build_requires = [
    # 'cmake-3',
]

private_build_requires = [
    'gcc',
    'ilmbase-2.4.1',
    'boost-1.70',
]

requires = [
    # 'boost-1.61',
    #'numpy'
]

variants = [["platform-linux"]]

uuid = "repository.%s" % name


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
