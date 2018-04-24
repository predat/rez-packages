name = "qt"

version = "4.8.6"

authors = [
    "Qt Company Ltd"
]

description = \
    """
    Qt is a cross-platform C++ application framework.
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = ["qmake"]

uuid = "repository.qt"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")

    if building:
        env.QTDIR = "{root}"
        env.QT_INCLUDE_DIR = "{root}/include"
        env.QT_LIB_DIR = "{root}/lib"
        env.QTLIB = "{root}/lib"
