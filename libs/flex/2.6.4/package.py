# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-flex

name = "flex"

version = "2.6.4"

authors = [
    "Will Estes"
]

description = \
    """
    The Fast Lexical Analyzer - scanner generator for lexing in C and C++.
    """

requires = [
    "bison-3+",
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "flex",
    "flex++"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "flex-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.FLEX_BINARY_PATH.set("{root}/bin")
    env.FLEX_INCLUDE_PATH.set("{root}/include")
    env.FLEX_LIBRARY_PATH.set("{root}/lib")
