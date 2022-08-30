# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-ilmbase

name = "pystring"

version = "1.1.3"

authors = [
    "Sony Picture Imageworks"
]

description = \
    """
    C++ functions matching the interface and behavior of python string methods with std::string
    """

requires = [
    "cmake-3.12+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pystring-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    env.PYSTRING_LIBRARY_PATH.set("{root}/lib")
    env.PYSTRING_INCLUDE_PATH.set("{root}/include")
