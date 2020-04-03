# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "qt"

version = "5.6.1-adsk"

authors = [""]

description = ""

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.qt"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
