# -*- coding: utf-8 -*-
#
from rez.utils.lint_helper import env


name = "muster"

version = "9.0.4"

authors = ["Vvertex"]

description = ""

requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = [
    'xConsole',
    'mrtool'
]

uuid = "repository.muster_console"


def commands():

    env.PATH.append("{root}")
    env.MUSTER = "{root}"
    env.MUSTER9 = "{root}"
