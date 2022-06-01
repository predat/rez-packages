# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-tinyxml
name = "tinyxml"

version = "2.6.2"

authors = [
    "Lee Thomason"
]

description = \
    """
    TinyXML is a simple, small, C++ XML parser that can be easily integrating into other programs.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "tinyxml-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.OCIO_INCLUDE_PATH.prepend("{root}/include")
    env.OCIO_LIBRARY_PATH.prepend("{root}/lib")
