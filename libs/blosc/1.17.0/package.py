# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-blosc

name = "blosc"

version = "1.17.0"

authors = [
    "Blosc Development Team"
]

description = \
    """
    Blosc is a high performance compressor optimized for binary data. It has been designed to transmit data to the
    processor cache faster than the traditional, non-compressed, direct memory fetch approach via a memcpy() OS call.
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

uuid = "blosc-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.BLOSC_INCLUDE_PATH.set("{root}/include")
    env.BLOSC_LIBRARY_PATH.set("{root}/lib")
