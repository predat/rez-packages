# -*- coding: utf-8 -*-

name = "pyilmbase"

version = "2.4.0"

description = \
    """
    """

private_build_requires = [
    'gcc-6.3.1',
    'ilmbase-2.4',
    'boost-1.70'
]

requires = [
    'numpy-1.16.5',
]

variants = [
    ["platform-linux", "python-2.7"],
    #["platform-linux", "python-3.7"]
]

uuid = "repository.%s" % name


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
