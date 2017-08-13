name = "oiio"

version = "1.7.16"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related classes, utilities, and applications.
    """

build_requires = [
    "python-2.7",
    "glew-1",
    "ilmbase-2.2.0",
    "openexr-2.2.0",
    "nuke"
]

requires = [
    "openexr-2.2",
    "glew-1",
    "boost-1.63",
    "ilmbase-2.2.0",
    "openexr-2.2.0"
]

variants = [
    ["platform-linux", "arch-x86_64"]
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

    if "nuke" in resolve:
        info("Loading OIIO Nuke plugins")
        env.NUKE_PATH.append("{root}/lib/nuke")
