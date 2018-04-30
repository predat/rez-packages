# -*- coding: utf-8 -*-
#
from rez.utils.lint_helper import env


name = "rv"

version = "7.2.2"

authors = ["RV"]

description = "RV player and tools"

requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = [
    'rv',
    'rvls',
    'rvio'
]

uuid = "repository.rv"


def commands():

    env.PATH.append("{root}/bin")
    env.OCIO = "/prod/project/LIBRARY_14_081/0_setup/color/config.ocio"
