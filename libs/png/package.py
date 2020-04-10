# -*- coding: utf-8 -*-


name = 'png'

version = '1.6.37'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

private_build_requires = ['gcc-6.3.1']

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
