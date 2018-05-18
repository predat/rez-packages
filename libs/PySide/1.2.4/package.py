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
        "qt",
        #"pip",
        #"setuptools",
        "shiboken",
        "python-2.7"
]

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "shiboken"
]

uuid = "repository.PySide"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
