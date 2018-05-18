# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, resolve


name = "ornatrix"

version = "2.1.3.15412"

authors = [""]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.ornatrix"

build_command = "bash {root}/install.sh"

plugin_for = ['maya']


def commands():

    env.LD_LIBRARY_PATH.append("{root}/Ephere/Plugins/Autodesk/Maya/Ornatrix/bin")
    env.MAYA_MODULE_PATH.append("{root}")
    env.ORNATRIX_MAYA_GROOMS_DIR = "{root}/Ephere/OrnatrixMaya/Grooms"
    env.ORNATRIXMAYA_LICENSE_SERVER_IP_PATH = "{root}/OrnatrixMayaLicenseServerIP.txt"

    if "mtoa" in resolve:
        import os
        env.MTOA_EXTENSIONS_PATH.append("{root}/Ephere/Plugins/Autodesk/Maya/Ornatrix/%s/extensions" % os.environ.get('MAYA_VERSION'))
        env.ORNATRIX_ARNOLD_PROCEDURAL_PATH.append("{root}/Ephere/Plugins/Autodesk/Maya/Ornatrix/%s/procedurals/OrnatrixProcedural.so" % os.environ.get('MAYA_VERSION'))
