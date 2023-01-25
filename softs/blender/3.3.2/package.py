# -*- coding: utf-8 -*-

name = 'blender'

version = '3.3.2'

description = """
Blender is the free and open source 3D creation suite.
LTS version.
"""

authors = ['Blender Foundation']

variants = [
    ['platform-linux'],
    ['platform-windows']
]

uuid = 'repository.%s' % name

with scope('config') as config:
    config.release_packages_path = '/s/apps/packages/cg'

tools = ['blender']

build_command = 'bash {root}/install.sh'


def commands():
    env.PATH.append('{root}')
    alias('blender', '{root}/blender')

