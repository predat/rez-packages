#From OSS-Pipeline from https://github.com/OSS-Pipeline/rez-xz

name = "xz"

version = "5.2.4"

authors = [
    "Lasse Collin"
]

description = \
    """
    XZ Utils is free general-purpose data compression software with a high compression ratio. XZ Utils were written
    for POSIX-like systems, but also work on some not-so-POSIX systems. XZ Utils are the successor to LZMA Utils.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "lzcat",
    "lzcmp",
    "lzdiff",
    "lzegrep",
    "lzfgrep",
    "lzgrep",
    "lzless",
    "lzma",
    "lzmadec",
    "lzmainfo",
    "lzmore",
    "unlzma",
    "unxz",
    "xz",
    "xzcat",
    "xzcmp",
    "xzdec",
    "xzdiff",
    "xzegrep",
    "xzfgrep",
    "xzgrep",
    "xzless",
    "xzmore"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "xz-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.XZ_BINARY_PATH.set("{root}/bin")
    env.XZ_INCLUDE_PATH.set("{root}/include")
    env.XZ_LIBRARY_PATH.set("{root}/lib")
