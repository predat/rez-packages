# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = 'glfw'

version = '3.2.1'

authors = ['']

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.glfw"


def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/glfw3/")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
