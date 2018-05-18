# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "openexr"

version = "2.2.0"

description = \
    """
    OpenEXR
    """

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.openexr"


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
