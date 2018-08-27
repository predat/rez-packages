# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "mtoa"

version = "3.0.1.1"

authors = ["SolidAngle"]

description = ""

variants = [
    ["platform-linux", "arch-x86_64", "maya-2016"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"],
    ["platform-linux", "arch-x86_64", "maya-2017"],
    ["platform-linux", "arch-x86_64", "maya-2018"]
]

plugin_for = ["maya"]

tools = [
    'kick',
    'oslc',
    'oslinfo',
    'maketx'
]

build_command = "bash {root}/build.sh {install}"

uuid = "repository.mtoa"


def commands():

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.MAYA_MODULE_PATH.append("{root}")
    env.MAYA_RENDER_DESC_PATH.append("{root}")
    env.MTOA_EXTENSIONS_PATH.append("{root}/extensions")
    env.solidangle_LICENSE = "5053@licarnold.prs.vfx.int"
