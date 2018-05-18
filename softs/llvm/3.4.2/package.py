# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "llvm"

version = "3.4.2"

authors = []

description = ''

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.llvm"


def commands():
    env.PATH.append("{root}/bin")
