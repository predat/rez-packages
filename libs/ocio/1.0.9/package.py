# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "ocio"

version = "1.0.9"

authors = [
]

description = \
    """
    """

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

tools = [
    "ociobakelut",
    "ociocheck",
    "ocioconvert",
    "ociodisplay",
    "ociolutimage"
]

uuid = "repository.ocio"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
