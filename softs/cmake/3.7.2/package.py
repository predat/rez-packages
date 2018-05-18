name = "cmake"

version = "3.7.2"

authors = [
    "Kitware"
]

description = \
    """
    Cross platform build system
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.cmake"

def commands():
    env.PATH.append("{root}/bin")
