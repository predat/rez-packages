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


name = "nuke_neatvideo"

version = "4.7.2"

authors = []

description = "Neat Video is a powerful video editing plug-in designed to reduce digital noise and other imperfections. It is an extremely effective way to clean up video from any source including video cameras, digitized film, TV tuners and others."

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.neatvideo"


# has_plugins = True
# plugin_for = ""

def commands():

    env.OFX_PLUGIN_PATH.append("{root}")
