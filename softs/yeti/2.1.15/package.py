# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building, resolve


name = "yeti"

version = "2.1.15"

authors = ["Peregrine Labs"]

description = ""

variants = [
    ["platform-linux", "arch-x86_64", "maya-2016.0"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"],
    ["platform-linux", "arch-x86_64", "maya-2017"],
]

plugin_for = ["maya"]

tools = []

build_command = "bash {root}/build.sh {install}"

uuid = "repository.yeti"


def commands():

    env.YETI_HOME = "{root}"
    env.YETI_TMP = "/tmp"
    env.peregrinel_LICENSE = "5053@licperegrinelabs.prs.vfx.int"
    # env.RLM_LICENSE = "5053@licperegrinelabs.prs.vfx.int"

    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.MAYA_MODULE_PATH.append("{root}")
    env.MAYA_SCRIPT_PATH.append("{root}/scripts")

    if "vray_maya" in resolve:
        vray_maya_version = env.MAYA_VERSION.value().replace('.', '_')
        env['VRAY_FOR_MAYA%s_PLUGINS_x64' % vray_maya_version].append("{root}/bin")
        env.VRAY_PLUGINS_x64.append("{root}/bin")

    if "mtoa" in resolve:
        env.MTOA_EXTENSIONS_PATH.append("{root}/plug-ins")
        env.ARNOLD_PLUGIN_PATH.append("{root}/bin")
        # env.MTOA_PROCEDURAL_PATH.append("{root}/bin")
