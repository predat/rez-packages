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

from rez.utils.lint_helper import env, building


name = "nuke_lenscare"

version = "1.44"

authors = []

description = ""

variants = [
    ["platform-linux", "arch-x86_64", "nuke"]
]

uuid = "repository.lenscare"

plugin_for = ["nuke"]


def commands():

    env.OFX_PLUGIN_PATH.prepend("{root}")
