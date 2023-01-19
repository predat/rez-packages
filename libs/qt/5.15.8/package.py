# -*- coding: utf-8 -*-

name = "qt"

version = "5.15.8"

description = """
The Qt framework contains a comprehensive set of highly intuitive and
modularized C++ library classes and is loaded with APIs to simplify your
application development.
"""

variants = [["platform-linux"]]

# requires = [
#     "html5lib",
#     "~python-3.7+<4"
# ]


private_build_requires = [
    "html5lib",
    #"nodejs-16+",
    "cmake-3",
    "python-3.7",
    "openssl-3",
    #"libxkbcommon-0.7",
    "llvm-15",
    "ninja",
    "gcc-9+",
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
