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


name = "shotgunapi"

version = "3.0.36"

authors = ["Shotgun Software"]

description = "Python-based API for accessing Shotgun"

variants = [["platform-linux", "arch-x86_64", "python-2.7"]]

tools = []

build_requires = ['setuptools']

uuid = "repository.shotgunapi"


def commands():
    env.PYTHONPATH.append("{root}/python")
