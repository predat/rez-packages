# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "blender"
version = "2.79b"
authors = ["Blender Foundation"]

description = "Blender"

requires = []

build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.blender"


def commands():
    env.PATH.append("{root}")
