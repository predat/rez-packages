# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "maya"

version = "2016.5.2"  # from mayapy -c "import maya.standalone; maya.standalone.initialize(name='python'); print maya.cmds.about(api=True); maya.standalone.uninitialize()"

authors = ["Autodesk"]

description = "Autodesk maya 2016 Extension 2 Service Pack 2"

build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = ["maya", "mayapy"]

uuid = "repository.maya"

has_plugins = True


def commands():

    env.MAYA_LOCATION.set("{root}/maya")
    env.MAYA_VERSION = "2016.5"

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")
    env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"
    env.MAYA_VP2_USE_GPU_MAX_TARGET_SIZE = 1

    env.PATH.prepend("{root}/maya/bin")
