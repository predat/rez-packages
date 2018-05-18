name = "oiio"

version = "1.5.24"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related classes, utilities, and applications.
    """

build_requires = [
    "gcc-4.8.3",
    "qt-4",
    "python-2.7",
    "glew-1"
]

requires = [
        "gcc-4.8.3",
        "openexr-2.2",
        "glew-1",
        "boost-1.63"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8", "python-2.7"]
]

tools = [
    "maketx",
    "iv",
    "igrep",
    "iinfo",
    "idiff",
    "iconvert"
    "oiiotool"
]


uuid = "repository.oiio"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.PYTHONPATH.append("{root}/lib/python/site-packages")
