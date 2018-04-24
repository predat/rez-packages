# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building, source, command


name = "houdini"

version = "16.5.439"

authors = ["SideFx"]

description = "Houdini version 16.5.439"

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    'houdini',
    'houdinifx',
    'mview',
    'mplay',
    'abcconvert',
    'abcinfo',
    'hbatch',
    'hcommand',
    'hcompile',
    'hserver',
    'hview',
    'hython',
    'mantra'
]

has_plugins = True

uuid = "repository.houdini"


def commands():

    command("rm -rf ~/.sesi_licenses.pref")

    env.SESI_LMHOST = "lichoudini.prs.vfx.int"

    source("{root}/houdini/houdini_setup_bash")

    env.PATH.prepend("{root}/houdini/bin")

    # if building:
    #     env.CMAKE_MODULE_PATH.append("{root}/cmake")
