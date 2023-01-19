# -*- coding: utf-8 -*-

name = "ninja"

version = "1.11.1"

description = "Ninja is a small build system with a focus on speed"

private_build_requires = ['gcc-9+', 'cmake-3+']

tools = ['ninja']

variants = [['platform-linux']]

uuid = 'repository.%s' % name


def commands():
    env.PATH.append('{root}/bin')
