# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building, source, command


name = "houdini"

version = "16.0.736"

authors = ["SideFx"]

description = "Houdini version 16.0.736"

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

    command("[[ -e ~/.sesi_licenses.pref ]] && /bin/rm -rf ~/.sesi_licenses.pref")
    env.SESI_LMHOST = "lichoudini.prs.vfx.int"
    env.PATH.prepend("{root}/houdini/bin")
    env.H = "{root}/houdini"
    env.HB = "{root}/houdini/bin"
    env.HDSO = "{root}/houdini/dsolib"
    env.HD = "{root}/houdini/demo"
    env.HH = "{root}/houdini/houdini"
    env.HHC = env.HH.value() + "/config"
    env.HT = "{root}/houdini/toolkit"
    env.HSB = env.HH.value() + "/sbin"

    env.TEMP = '/tmp'
