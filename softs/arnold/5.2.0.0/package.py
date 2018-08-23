# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "arnold"

version = "5.2.0.0"

authors = ["SolidAngle"]

description = ""

variants = [
    ["platform-linux", "arch-x86_64"],
]

tools = [
    'kick',
    'oslc',
    'oslinfo',
    'maketx'
]

build_command = "bash {root}/install.sh"

uuid = "repository.arnold"


def commands():

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
    env.solidangle_LICENSE = "5053@licarnold.prs.vfx.int"
