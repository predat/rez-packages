# -*- coding: utf-8 -*-

# Copyright (C) Fix Studio, and/or its licensors.
# All rights reserved.
#
# The coded instructions, statements, computer programs, and/or related
# material (collectively the "Data") in these files contain unpublished
# information proprietary to Fix Studio and/or its licensors.
#
# The Data may not be disclosed or distributed to third parties or be
# copied or duplicated, in whole or in part, without the prior written
# consent of Fix Studio.

from rez.utils.lint_helper import env, building


name = "hdrlight_maya"

version = "2018.0202"

authors = ["Lightmap"]

description = ""

variants = [
    ["platform-linux", "arch-x86_64", "maya-2016.5"],
    ["platform-linux", "arch-x86_64", "maya-2017"],
    ["platform-linux", "arch-x86_64", "maya-2018"]
]

uuid = "repository.hdrlight_maya"

build_command = "bash {root}/install.sh"

requires = ["hdrlight-5"]


def commands():

    env.MAYA_MODULE_PATH.append("{root}")
    env.HDRLS_HOME_V5 = env.REZ_HDRLIGHT_ROOT.value()
