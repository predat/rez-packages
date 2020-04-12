# -*- coding: utf-8 -*-

name = 'yasm'

version = '1.3.0'

variants = [['platform-linux']]

private_build_requires = ['gcc-6.3.1', 'cmake-3+']

description = """
Yasm is a complete rewrite of the NASM assembler under the “new” BSD License
(some portions are under other licenses, see COPYING for details).
"""

tools = [
    'yasm'
]


def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
