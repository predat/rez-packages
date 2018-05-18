name = "ocio_nuke"

version = "1.0.9"

authors = [
]

description = \
    """
    """

build_requires = [
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
    "ocio"
    #"ilmbase-2.2.0",
    #"openexr-2.2.0"
]

variants = [
    ["platform-linux", "arch-x86_64", "nuke-10.0v6"],
    ["platform-linux", "arch-x86_64", "nuke-10.5v4"]
]

tools = []


uuid = "repository.ocio_nuke"

def commands():

    version_short = str(env.REZ_NUKE_VERSION).split('v')[0]
    env.NUKE_PATH.append("{root}/lib/nuke" + version_short)
