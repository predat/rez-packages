# -*- coding: utf-8 -*-


name = 'freeglut'

version = '3.2.1'

variants = [['platform-linux']]

uuid = 'repository.%s' % name

private_build_requires = [
    'gcc-6.3.1',
    'cmake-3'
]


def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.CMAKE_PREFIX_PATH.append('{root}')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
