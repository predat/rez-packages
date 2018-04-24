name = "binutils"

version = "2.25"

authors = [
    "GNU"
]

description = \
    """
    GNU project C and C++ compiler.
    """

variants = [
    ["platform-linux", "arch-x86_64"],
]

tools = [
    "addr2line",
    "ar",
    "as",
    "c++filt",
    "elfedit",
    "gprof",
    "ld",
    "ld.bfd",
    "nm",
    "objcopy",
    "objdump",
    "ranlib",
    "readelf",
    "size",
    "strings",
    "strip"
]

uuid = "repository.binutils"

def commands():
    env.PATH.append("{root}/bin")

    # if building:
    #     env.CC = "{root}/bin/gcc"
    #     env.CXX = "{root}/bin/g++"
