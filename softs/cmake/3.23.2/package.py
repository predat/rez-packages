# Based and improved from https://github.com/piratecrew/rez-cmake
# And then taken from https://github.com/OSS-Pipeline/rez-cmake

name = "cmake"

version = "3.23.2"

authors = [
    "Andy Cedilnik",
    "Bill Hoffman",
    "Brad King",
    "Ken Martin",
    "Alexander Neundorf"
]

description = \
    """
    CMake is a cross-platform free and open-source software tool for managing the build process
    of software using a compiler-independent method.
    """

requires = [
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "cmake"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "cmake-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")

    # Helper environment variables.
    env.CMAKE_BINARY_PATH.set("{root}/bin")
