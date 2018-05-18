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

version = "3.2.15.1"

authors = [""]

description = ""

plugin_for = ["maya"]

requires = ["maxwell-3", "maya"]

variants = [
    ["platform-linux", "arch-x86_64", "maya-2016"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"],
    ["platform-linux", "arch-x86_64", "maya-2017"],
    #  ["platform-linux", "arch-x86_64", "maya-2018"]  # does not exists for 2018 ??
]

build_requires = []

tools = []

uuid = "repository.maxwell_maya"


def commands():

    env.MAYA_PLUG_IN_PATH.append("{root}/bin/plug-ins")

    env.MAYA_SCRIPT_PATH.append("{root}/scripts/AETemplates")
    env.MAYA_SCRIPT_PATH.append("{root}/scripts/others")

    env.XBMLANGPATH.append("{root}/icons/%B")

    env.MAYA_RENDER_DESC_PATH.append("{root}/bin/rendererDesc")
