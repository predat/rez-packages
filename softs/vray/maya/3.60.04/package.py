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

from rez.utils.lint_helper import env, building, info


name = "vray_maya"

version = "3.60.04"

authors = ['Choas Group']

description = """
    Production-proven ray traced rendering with a full suite of tools
    to create professional photoreal imagery and animations."""

variants = [
    ["platform-linux", "arch-x86_64", "maya-2016.0"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"],
    ["platform-linux", "arch-x86_64", "maya-2017.0"],
    ["platform-linux", "arch-x86_64", "maya-2018.0"],
]

tools = [
    "vray",
]

plugin_for = ["maya"]

uuid = "repository.vray_maya"

build_command = "bash {root}/install.sh"


def commands():

    env.VRAY_AUTH_CLIENT_FILE_PATH = "{root}"
    env.MAYA_RENDER_DESC_PATH.append("{root}/maya_root/bin/rendererDesc")
    vray_maya_version = env.MAYA_VERSION.value().replace('.', '_')
    env['VRAY_FOR_MAYA%s_MAIN_x64' % vray_maya_version].append("{root}/maya_vray")
    env['VRAY_FOR_MAYA%s_PLUGINS_x64' % vray_maya_version].append("{root}/maya_vray/vrayplugins")
    env['VRAY_OSL_PATH_MAYA%s_x64' % vray_maya_version].append("{root}/vray/opensl")

    # env.PATH.append("{root}/maya_root/bin")
    env.LD_LIBRARY_PATH.append("{root}/maya_root/lib")
    env.MAYA_PLUG_IN_PATH.append("{root}/maya_vray/plug-ins")
    env.MAYA_SCRIPT_PATH.append("{root}/maya_vray/scripts")
    env.PYTHONPATH.append("{root}/maya_vray/scripts")
    env.XBMLANGPATH.append("{root}/maya_vray/icons/%B")
