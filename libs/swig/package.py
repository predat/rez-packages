# -*- coding: utf-8 -*-

name = 'swig'

version = '4.0.1'

description = """
SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages.
"""

authors = ['']

variants = [
    ['platform-linux', 'python-2.7'],
    ['platform-linux', 'python-3.7']
]

requires = []

private_build_requires = [
    'gcc-6.3.1',
    'cmake-3+',
    'boost-1.70',
]

uuid = 'repository.%s' % name


def commands():
    env.PATH.append('{root}/bin')
