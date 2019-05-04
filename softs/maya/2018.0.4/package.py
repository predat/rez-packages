# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


def _version():
    import os
    return os.path.basename(os.getcwd())


name = "maya"
version = _version()
authors = ["Autodesk"]
description = "Autodesk maya %s Update 4" % version.split('.')[0]
variants = [["platform-linux"]]
tools = [
    'maya',
    'maya%s' % version.split('.')[0],
    'Render',
    'mayapy',
    "register_maya"]
has_plugins = True
uuid = "repository.maya"


def commands():

    import os
    env.MAYA_VERSION = str(this.version.major)
    env.MAYA_LOCATION.set(os.path.join("{root}", "maya"))

    env.PATH.prepend(os.path.join("{root}", "bin"))
    # env.PATH.prepend(os.path.join("{root}", "maya", "bin"))
    env.PATH.prepend(os.path.join("$MAYA_LOCATION", "bin"))

    env.LD_LIBRARY_PATH.append(os.path.join("$MAYA_LOCATION", "lib"))

    env.PYTHONPATH.append("{root}/maya/lib/python2.7/site-packages")

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")

    # env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    # env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    if building:
        env.CMAKE_MODULE_PATH.append(os.path.join("{root}", "cmake"))
