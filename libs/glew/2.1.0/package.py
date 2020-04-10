# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'glew'

version = '2.1.0'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

private_build_requires = ['gcc-6.3.1']


def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
