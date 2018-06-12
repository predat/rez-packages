# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "cryptomatte_nuke"

version = "1.2.0"

authors = ["Psyop"]

description = """
Cryptomatte is a tool created at Psyop by Jonah Friedman and Andy Jones.
It creates ID mattes automatically with support for motion blur, transparency,
and depth of field, using organizational information already available at
render time. This organizational information is usually names, object
namespaces, and material names.
"""

requires = ['nuke']

plugin_for = ["nuke"]

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.cryptomatte_nuke"


def commands():
    env.NUKE_PATH.append('{root}/nuke')
