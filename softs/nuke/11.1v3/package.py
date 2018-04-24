# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, alias, building


name = "nuke"

version = "11.1.3"

authors = ["Foundry"]

description = "Nuke 11.1v3"

variants = [["platform-linux", "arch-x86_64"]]

tools = ['nuke']

has_plugins = True

uuid = "repository.nuke"


def commands():

    env.PATH.prepend("{root}/nuke")
    env.foundry_LICENSE = "4101@licfoundry.prs.vfx.int"

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
