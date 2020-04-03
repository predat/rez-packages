# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = 'tiff'

version = '4.0.8'

authors = ['fredrik.brannbacka']

variants = [
    ["platform-linux"]
]

private_build_requires = [
    "gcc-6.3.1",
    "jpeg",
    #"zlib"
]

uuid = 'repository.tiff'


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
