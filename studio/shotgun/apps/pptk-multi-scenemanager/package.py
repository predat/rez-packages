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

from rez.utils.lint_helper import env, getenv, building, scope  # make linter happy


name = 'pptk_multi_scenemanager'

version = '1.0.0'

build_requires = []

requires = [
    'fixstudio',
    'ppma'
]

variants = [
    ["python-2.7"]
]

uuid = 'repository.pptk_multi_scenemanager'

tools = []

# with scope("config"):
#     release_packages_path = "/prod/softprod/rez-packages/int"


def commands():
    pass
