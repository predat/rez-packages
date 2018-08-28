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


name = "qt5"
version = "5.11.1"
authors = [""]
description = ""
variants = [["platform-linux", "arch-x86_64"]]
uuid = "repository.qt5"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")
