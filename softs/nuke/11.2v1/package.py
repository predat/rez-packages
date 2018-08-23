# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, alias, building


name = "nuke"

version = "11.2.1"

authors = ["Foundry"]

description = "Nuke 11.2v1"

variants = [["platform-linux", "arch-x86_64"]]

tools = ['nuke']

has_plugins = True

uuid = "repository.nuke"


def commands():

    env.PATH.prepend("{root}/nuke")
    env.foundry_LICENSE = "4101@licfoundry.prs.vfx.int"
    env.FN_DISABLE_LICENSE_DIALOG = 1  # suppress temporary license dialog

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
