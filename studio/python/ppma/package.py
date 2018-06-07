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

from rez.utils.lint_helper import env, building, scope  # male linter happy


name = 'ppma'

version = '1.0.0.2'

build_requires = []

requires = ['pppy', 'maya', 'shotgunapi']

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

uuid = 'repository.ppma'

# with scope("config"):
#     release_packages_path = "/prod/softprod/rez-packages/int"


def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/setup")
    env.PYTHONPATH.append("{root}/python")
    env.PP_PIPE_MAYA_COMMON_PATH = "{root}/common"
