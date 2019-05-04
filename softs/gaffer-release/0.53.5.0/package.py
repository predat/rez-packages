# -*- coding: utf-8 -*-

name = "gaffer"

def _version():
    import os
    return os.path.basename(os.getcwd())


version = _version()

description = ""

authors = [""]

build_requires = []

build_command = "bash {root}/install.sh"

requires = []

tools = ['gaffer']

help = ""

has_plugins = False

uuid = "repository.gaffer"


def commands():
    import os
    env.PATH.append(os.path.join('{root}', 'bin'))
