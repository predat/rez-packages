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


name = "mentalray"

version = "3.13.1.11"

authors = ["NVidia"]

description = ""

variants = [
    ["platform-linux", "arch-x86_64", "maya-2016.0"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"]
]

uuid = "repository.mentalray"

plugin_for = ['maya']

build_command = "bash {root}/install.sh"


def commands():

    env.MAYA_MODULE_PATH.append("{root}")
