# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'libYaml'

version = '0.2.2'

variants = [["platform-linux"]]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.ZLIB_ROOT.set("{root}")
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
