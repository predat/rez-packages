# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "maya"

version = "2018.0.2"  # Version: 20#.EXT.SP

authors = ["Autodesk"]

description = "Autodesk maya 2018 Update 2"

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    'maya',
    'maya2018',
    'Render',
    'mayapy',
    "register_maya"
]

has_plugins = True

uuid = "repository.maya"


def commands():

    env.MAYA_VERSION = "2018"
    env.MAYA_LOCATION.set("{root}/maya")
    env.PATH.prepend("{root}/maya/bin")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/maya/lib")
    env.PYTHONPATH.append("{root}/maya/lib/python2.7/site-packages")

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")
    env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
