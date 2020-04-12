# -*- coding: utf-8 -*-

#from rez.utils.lint_helper import env, building

name = 'llvm'

version = '8.0.1'

authors = []

description = ''


private_build_requires = [
    'gcc-6.3.1',
    'cmake-3+',
    'swig-4',
    'python-2.7',
    'ninja',
    'yasm'
]

variants = [["platform-linux"]]

uuid = "repository.%s" % name

build_command = 'bash {root}/install.sh {install}'


def commands():
    env.PATH.append("{root}/bin")
    env.CC='clang'
    env.CXX='clang++'

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")


