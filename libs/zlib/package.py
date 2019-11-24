# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'zlib'

version = '1.2.11'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
