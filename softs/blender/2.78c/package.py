name = "blender"
version = "2.78c"
authors = ["Blender Foundation"]

description = \
    """
    Blender
    """

requires = [
    "oiio",
    "glew"
]

build_requires = [
    "openexr",
    "ilmbase"
]

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.blender"


def commands():
    env.PATH.append("{root}/bin")
