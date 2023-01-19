# -*- coding: utf-8 -*-

name = "qt"

version = "6.4.2"

description = """
The Qt framework contains a comprehensive set of highly intuitive and modularized C++ library classes and is loaded with APIs to simplify your application development.
"""

variants = [
    ["platform-linux", "build-release"],
    ["platform-linux", "build-debug"],

]

# requires = [
#     "libxkbcommon-0.7"
# ]

private_build_requires = [
    "cmake-3",
    "git",
    "ninja",
    "python-3.7",
    "llvm-15",
    "openssl-3",
    "zlib-1.12",
    "gcc-9+",
    "html5lib",
]

with scope("config") as config:
    config.release_packages_path = "/s/apps/packages/dev"

tools = [
    "designer",
    "assistant",
    "qml",
    "qmake",
    "qpaths"
]


def commands():
    env.PATH.append("{root}/bin")
    env.QT_PLUGIN_PATH.append("{root}/plugins")
    env.QT_QPA_PLATFORM_PLUGIN_PATH = "{root}/plugins/platforms"
    env.QML2_IMPORT_PATH.append("{root}/qml")

    if system.platform == "linux":
        env.LD_LIBRARY_PATH.append("{root}/lib")
        if building:
            env.QMAKESPEC = "{root}/mkspecs/linux-g++"
    else:  # osx
        env.DYLD_FRAMEWORK_PATH.append("{root}/lib")
        if building:
            env.QMAKESPEC = "{root}/mkspecs/macx-clang"

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.QTDIR = "{root}"
