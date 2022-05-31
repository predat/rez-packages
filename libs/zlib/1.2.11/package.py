# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-zlib

name = "zlib"

version = "1.2.11"

authors = [
    "Jean-Loup Gailly",
    "Mark Adler"
]

description = \
    """
    zlib is designed to be a free, general-purpose, legally unencumbered -- that is, not covered by any patents --
    lossless data-compression library for use on virtually any computer hardware and operating system.
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

uuid = "zlib-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/share/pkgconfig")

    # Helper environment variables.
    env.ZLIB_INCLUDE_PATH.set("{root}/include")
    env.ZLIB_LIBRARY_PATH.set("{root}/lib")
