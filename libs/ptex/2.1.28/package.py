# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope


name = "ptex"

version = "2.1.28"

variants = [["platform-linux", "arch-x86_64"]]


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
