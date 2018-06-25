# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'png'

version = '1.6.29'

authors = ['fredrik.brannbacka']

variants = [["platform-linux", "arch-x86_64"]]


def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
