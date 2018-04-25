# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "mtoa"

version = "3.0.0.2"

authors = ["SolidAngle"]

description = ""

variants = [
    ["platform-linux", "arch-x86_64", "maya-2017"],
    ["platform-linux", "arch-x86_64", "maya-2018"]
]

tools = [
    'kick'
]

build_command = "bash {root}/build.sh {install}"

uuid = "repository.mtoa"


def commands():

    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/maya/lib/python2.7/site-packages")

    env.MAYA_MODULE_PATH = "{root}"
    env.MAYA_RENDER_DESC_PATH = "{root}"
