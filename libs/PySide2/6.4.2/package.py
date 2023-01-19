# -*- coding: utf-8 -*-

name = "pyside6"

version = "6.4.2"

description = "Python bindings for the Qt cross-platform application and UI framework"

requires = ["python-3.7+<4"]

private_build_requires = [
    "numpy",
    "cmake-3",
    "pyopengl",
    #"six",
    "ninja",
    "openssl-3",
    "packaging-21.3+",
    "setuptools",
    # "wheel-0.37",
    # "pybuild-0.8",
    "llvm-15",
    #"libxkbcommon",
    "gcc-9+",
]

variants = [
    ["platform-linux", "build-release", "qt-6.4.2"],
    ["platform-linux", "build-debug", "qt-6.4.2", "python-3.7"],
    ["platform-linux", "build-debug", "qt-6.4.2", "python-3.9"],
]

tools = [
    "rcc",
    "uic",
    "pyside2-uic",
    "shiboken2",
    "pyside6-designer",
    "pyside_tool.py"
]

uuid = "repository.%s" % name

# with scope("config") as config:
#     config.release_packages_path = "/s/apps/packages/dev"


def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python')

    alias("designer", "{root}/bin/pyside6-designer")
    alias("assistant", "{root}/bin/pyside6-assistant")
    alias("uic", "{root}/bin/pyside6-uic")
    alias("rcc", "{root}/bin/pyside6-rcc")
