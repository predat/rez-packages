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


name = 'pppy'

version = '1.0.0'

build_requires = []

requires = ['pip', 'tk_core', 'requests', 'pyseq', 'lxml', 'PyYAML', 'fixstudio']

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

uuid = 'repository.pppy'

tools = [
    'pp-clean-project',
    'pp-create-delivery',
    'pp-create-discreet-project',
    'pp-create-or-update-qt',
    'pp-create-project',
    'pp-create-sgtk-project',
    'pp-launch-action',
    'pp-launch-app-bin',
]

# with scope("config"):
#     release_packages_path = "/prod/softprod/rez-packages/int"


def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
