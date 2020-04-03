# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = 'jpeg'

version = '1.5.2'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

uuid = "repository.jpeg"

private_build_requires = ["gcc-6.3.1"]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
