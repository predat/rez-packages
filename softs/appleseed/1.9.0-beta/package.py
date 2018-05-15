# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, resolve


name = "appleseed"
version = "1.9.0-beta"
authors = [""]

description = "Appleseed Rendering engine"

requires = []

build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.appleseed"

tools = [
    'appleseed.cli',
    'appleseed.studio',
    'oiiotool',
    'maketx',
    'oslc',
    'oslinfo'
]


def commands():
    env.APPLESEED.set("{root}")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")
    env.OCIO = "{root}/ocio/config.ocio"

    if 'gaffer' in resolve:
        env.OSL_SHADER_PATHS.append("{root}/shaders/appleseed")
        env.APPLESEED_SEARCHPATH.append("{root}/shaders/appleseed")
