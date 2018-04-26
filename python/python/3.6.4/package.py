# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "python"

version = "3.6.4"

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
    "python3",
    "python3-config",
]

uuid = "repository.python3"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python3.6"
        env.PYTHON_LIBRARIES = "{root}/lib/python3.6/config/libpython3.6.a"
