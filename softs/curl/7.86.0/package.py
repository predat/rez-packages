# -*- coding: utf-8 -*-

name = "curl"

version = "7.86.0"

requires = [
    "zlib-1.2",
    "openssl-3"]

build_requires = [
    "cmake-3",
    "gcc-9+",]

variants = [["platform-linux"]]

tools = ["curl"]

description = """
curl is used in command lines or scripts to transfer data.
"""

uuid = "repository.%s" % name


def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.CMAKE_PREFIX_PATH.append('{root}')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
