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


name = "maya"

version = "2017.0.60"  # from mayapy -c "import maya.standalone; maya.standalone.initialize(name='python'); print maya.cmds.about(api=True); maya.standalone.uninitialize()"

authors = ["Autodesk"]

description = "Autodesk maya 2017 Update 4"

build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = ["maya", "mayapy"]

uuid = "repository.maya"


def commands():
    env.MAYA_LOCATION.set("{root}/maya")
    env.PATH.prepend("{root}/maya/bin")
    env.PATH.prepend("{root}/bin")

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")

    env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    env.MAYA_VERSION = 2017
