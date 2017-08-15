name = "oiio_nuke"
version = "1.7.16"
authors = ["Larry Gritz"]
description = \
    """
    OpenImageIO Nuke Plugins
    """
build_requires = [
    "boost-1.63",
    "oiio",
    #"glew-1",
    "ilmbase-2.2.0",
    "openexr-2.2.0",
    "nuke"
]
requires = [
    #"oiio",
    #"openexr-2.2",
    #"glew-1",
    #"boost-1.63",
    #"ilmbase-2.2.0",
    #"openexr-2.2.0",
]
variants = [
    ["platform-linux", "arch-x86_64", "nuke-10.5v4"],
    ["platform-linux", "arch-x86_64", "nuke-10.0v6"]
]
tools = []
build_command = "python {root}/install.py"
plugin_for = ["nuke"]
uuid = "repository.oiio_nuke"


def commands():
    #if "nuke" in resolve:
    #    info("Loading OIIO Nuke plugins")
    env.NUKE_PATH.append("{root}")
