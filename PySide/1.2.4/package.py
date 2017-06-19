name = "PySide"

version = "1.2.4"

authors = [
    ""
]

description = \
    """
    The PySide project provides LGPL-licensed Python bindings for the Qt.
    """

requires = [
        "qt-4.8.6",
        "pip",
        "setuptools",
        "shiboken",
        "python-2.7"
]

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8", "python-2.7"]
]

uuid = "repository.PySide"

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
