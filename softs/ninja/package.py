# -*- coding: utf-8 -*-

name = "ninja"

version = "1.10.0"

description = "Ninja is a small build system with a focus on speed"

private_build_requires = ['gcc-6.3.1', 'cmake-3+']

tools = ['ninja']

variants = [['platform-linux']]

uuid = 'repository.%s' % name


def commands():
    env.PATH.append('{root}/bin')
