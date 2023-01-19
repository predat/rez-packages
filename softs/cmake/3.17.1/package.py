# -*- coding: utf-8 -*-

name = "cmake"

version = "3.17.1"

authors = ["Kitware"]

description = \
    """
    Cross platform build system
    """

private_build_requires = []

variants = [["platform-linux"]]

uuid = "repository.%s" % name

tools = [
    "ccmake",
    "cmake",
    "cpack",
    "ctest"
]


def commands():
    env.PATH.append("{root}/bin")
