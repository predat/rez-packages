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

from rez.utils.lint_helper import env, building  # make linter happy


name = "maxwell_maya"

version = "4.2.1.0"

authors = [""]

description = ""

plugin_for = ["maya"]

# requires = ["maxwell-4.2", "maya"]
requires = ["maxwell-4.2"]

variants = [
    # ["platform-linux", "arch-x86_64", "maya-2016"],
    ["platform-linux", "arch-x86_64", "maya-2017"],
    ["platform-linux", "arch-x86_64", "maya-2018"]
]

build_requires = []

requires = ["maxwell", "maya"]

tools = []

uuid = "repository.maxwell_maya"


def commands():

    env.MAYA_PLUG_IN_PATH.append("{root}/bin/plug-ins")

    env.MAYA_SCRIPT_PATH.append("{root}/scripts/AETemplates")
    env.MAYA_SCRIPT_PATH.append("{root}/scripts/others")

    env.XBMLANGPATH.append("{root}/icons/%B")

    env.MAYA_RENDER_DESC_PATH.append("{root}/bin/rendererDesc")
