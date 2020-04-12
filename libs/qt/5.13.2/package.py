# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "qt"

version = "5.13.2"

authors = [""]

description = ""

variants = [["platform-linux"]]

private_build_requires = ['gcc-6.3.1']

uuid = "repository.qt"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
