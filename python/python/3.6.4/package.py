# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "python"

@early()
def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

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
    ["platform-linux"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python3",
    "python3-config",
]

uuid = "repository.python"


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python3.6"
        env.PYTHON_LIBRARIES = "{root}/lib/python3.6/config/libpython3.6.a"
