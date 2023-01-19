# -*- coding: utf-8 -*-

name = "git"

version = "2.39.1"

build_requires = [
    "cmake-3",
    "gcc-9+",
    "zlib-1.2",
    "openssl-3",
    "curl-7.86"
]

variants = [["platform-linux"]]

tools = [
    "git",
    "gitk",
    "git-shell",
    "git-upload-pack",
    "git-cvsserver",
    "git-receive-pack",
    "git-upload-archive",
    "scalar"
]

description = """
Git is a fast, scalable, distributed revision control system with an unusually
rich command set that provides both high-level operations and full access to internals.
"""

uuid = "repository.%s" % name


def commands():
    env.PATH.append('{root}/bin')

