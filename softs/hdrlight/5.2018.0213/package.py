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


name = "hdrlight"

version = "5.2018.0213"

authors = ["Lightmap"]

description = ""

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.hdrlight"

build_command = "bash {root}/install.sh"


def commands():

    env.PATH.append("{root}")
    env.lightmap_LICENSE = "7053@lichdrlightstudio.prs.vfx.int"
