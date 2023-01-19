# -*- coding: utf-8 -*-

name = 'swig'

version = '4.1.1'

description = """
SWIG is a software development tool that connects programs written in C and C++
with a variety of high-level programming languages.
"""

variants = [
    ['platform-linux', 'python-2.7'],
    ['platform-linux', 'python-3.7'],
    ['platform-linux', 'python-3.9']
]

requires = []

private_build_requires = [
    'gcc-9+',
    'cmake-3+',
    'boost-1.80',
]

uuid = 'repository.%s' % name


def commands():
    env.PATH.append('{root}/bin')
