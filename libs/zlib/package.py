# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'zlib'

version = '1.2.11'

authors = ['fredrik.brannbacka']

variants = [["platform-linux", "arch-x86_64"]]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.ZLIB_ROOT.set("{root}")
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
