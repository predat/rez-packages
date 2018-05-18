# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "boost"

version = "1.56.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.boost"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.BOOST_ROOT = '{root}'

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
