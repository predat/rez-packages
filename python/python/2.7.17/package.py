# -*- coding: utf-8 -*-

name = 'python'
version = '2.7.17'
authors = ["Guido van Rossum"]
description = """The Python programming language."""

uuid = 'repository.%s' % name

variants = [
    ["platform-linux", "build-release"],
    ["platform-linux", "build-debug"],
    #["platform-osx", "build-release"],
    #["platform-osx", "build-debug"],
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

private_build_requires = ['gcc-6.3.1']


def commands():
    env.PATH.prepend('{root}/bin')

    if system.platform == 'osx':
        env.DYLD_LIBRARY_PATH.append("{root}/lib")
    elif system.platform == 'linux':
        env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
