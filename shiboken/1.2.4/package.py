name = "shiboken"

version = "1.2.4"

authors = [
    "pyside"
]

description = \
    """
    Python bindings generator that uses API Extractor and outputs CPython code.
    """

requires = [
    "qt-4.8.6"
]

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8", "python-2.7"]
]

uuid = "repository.shiboken"

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.SHIBOKEN_INCLUDE_DIR.append('{root}/include')

