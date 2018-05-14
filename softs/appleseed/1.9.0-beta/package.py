# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


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
    env.PATH.append("{root}/bin")
    env.OCIO = "{root}/ocio/config.ocio"
