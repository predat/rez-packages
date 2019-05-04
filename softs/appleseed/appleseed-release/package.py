# -*- coding: utf-8 -*-

name = "appleseed"

version = "2.0.0-beta"

description = "Appleseed Renderer"

build_command = "bash {root}/install.sh"

requires = []

variants = [['platform-linux']]


def commands():
    import os
    env.PATH.append(os.path.join('{root}', 'bin'))
    env.LD_LIBRARY_PATH.prepend(os.path.join('{root}', 'lib'))
    env.PYTHONHOME = this.root

    env.APPLESEED = this.root
