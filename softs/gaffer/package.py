# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "gaffer"

version = "0.47.0.0"

authors = ["Image Engine"]

description = \
    """
Gaffer is an open source application framework designed specifically for creating tools for use in visual effects production. It builds on top of the Cortex libraries, adding a flexible node-based computation framework and a user interface framework for editing and viewing node graphs. Gaffer ships with a number of sample modules and applications, not least of which is a module for the on-demand generation of procedural scenes for rendering.
    """
build_requires = []

requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = [
    "ffmpeg",
    "ffprobe",
    "ffserver"
]

uuid = "repository.gaffer"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
