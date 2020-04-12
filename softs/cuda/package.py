# -*- coding: utf-8 -*-

name='cuda'

version='9.2'

variants = [['platform-linux']]

uuid = 'repository.%s' % name

build_command = 'bash {root}/install.sh'

private_build_requires = ['gcc-6.3.1', 'cmake-3+']


def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.LD_LIBRARY_PATH.append('{root}/lib64')
        env.CMAKE_PREFIX_PATH.append('{root}')
        env.CUDA_TOOLKIT_ROOT_DIR = '{root}'
        env.CUDA_BIN_PATH = '{root}'

