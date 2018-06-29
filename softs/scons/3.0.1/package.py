# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "scons"

version = "3.0.1"

authors = ['']

description = \
    """
SCons is an Open Source software construction tool—that is, a next-generation build tool. Think of SCons as an improved, cross-platform substitute for the classic Make utility with integrated functionality similar to autoconf/automake and compiler caches such as ccache. In short, SCons is an easier, more reliable and faster way to build software.
    """

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]


build_requires = [
]

requires = [
]

tools = []

uuid = "repository.scons"


def commands():
    env.PYTHONPATH.append("{root}/lib/scons-{version}")
    env.PATH.append("{root}/bin")
