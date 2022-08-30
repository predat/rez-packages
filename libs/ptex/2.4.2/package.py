# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-ptex

name = "ptex"

version = "2.4.2"

authors = [
    "Walt Disney Animation Studios"
]

description = \
    """
    Ptex is a texture mapping system developed by Walt Disney Animation Studios for production-quality rendering.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "ptxinfo"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "ptex-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    # Helper environment variables.
    env.PTEX_BINARY_PATH.set("{root}/bin")
    env.PTEX_INCLUDE_PATH.set("{root}/include")
    env.PTEX_LIBRARY_PATH.set("{root}/lib64")
