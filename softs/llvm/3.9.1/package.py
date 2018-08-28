# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "llvm"

version = "3.9.1"

authors = []

description = ''

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.llvm"

tools = [
    'llvm-ar',
    'clang'
]


def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/share/llvm/cmake")
        env.CMAKE_MODULE_PATH.append("{root}/share/clang/cmake")
