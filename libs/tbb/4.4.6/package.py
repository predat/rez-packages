# -*- coding: utf-8 -*-
#
from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "tbb"

version = "4.4.6"

variants = [
    ["platform-linux", "arch-x86_64"]
]


def commands():
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
