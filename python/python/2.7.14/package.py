# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "python"

version = "2.7.14"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

build_requires = [
    # "gcc-4.8.2"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

uuid = "repository.python"


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
