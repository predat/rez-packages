name = "ocio"

version = "1.0.9"

authors = [
]

description = \
    """
    """

build_requires = [
    "python-2.7",
    "glew-1",
    "ilmbase-2.2.0",
    "openexr-2.2.0",
    "oiio",
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
    "ociobakelut",
    "ociocheck",
    "ocioconvert",
    "ociodisplay",
    "ociolutimage"
]


uuid = "repository.ocio"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python/site-packages")

    if building:
        env.OCIO_INCLUDE_DIR = "{root}/include"

    if "nuke" in resolve:
        info("Loading OCIO Nuke plugins")
        env.NUKE_PATH.append("{root}/lib/nuke")
