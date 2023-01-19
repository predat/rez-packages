# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "llvm"

version = "15.0.6"

authors = ["llvm"]

description = """
The LLVM project has multiple components. The core of the project is itself
called "LLVM". This contains all of the tools, libraries, and header files
needed to process intermediate representations and convert them into object
files. Tools include an assembler, disassembler, bitcode analyzer, and bitcode
optimizer. It also contains basic regression tests.
"""

private_build_requires = ["gcc-9+", "cmake-3+", "swig", "ninja", "python-3.7"]

variants = [["platform-linux"]]

uuid = "repository.llvm"

# with scope("config") as config:
#     config.release_packages_path = "/s/apps/packages/dev"

build_command = "bash {root}/install.sh"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.CC = "clang"
    env.CXX = "clang++"

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
