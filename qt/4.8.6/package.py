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
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8"]
]

uuid = "repository.qt"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
