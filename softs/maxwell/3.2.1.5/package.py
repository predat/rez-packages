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


name = "maxwell"

version = "3.2.1.5"

authors = ["Next Limit"]

description = ""

variants = [["platform-linux", "arch-x86_64"]]

build_requires = []

requires = []

tools = [
    "maxwell",
    "mxed",
    "patchelf",
    "mximerge",
    "pymaxwell"
    "studio"
]

uuid = "repository.maxwell"


def commands():

    env.MAXWELL_ROOT = "{root}"
    env.MAXWELL3_ROOT = "{root}"
    env.MAXWELL3_MATERIALS_DATABASE = "{root}/materials database"
    env.MAXWELL_HONOR_UMASK = 1
    env.nextlimit_LICENSE = "8053@licmaxwell.prs.vfx.int"

    env.PATH.append("{root}")
    env.LD_LIBRARY_PATH.append("{root}")
