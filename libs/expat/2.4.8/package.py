name = "expat"

version = "2.4.8"

authors = [
    "James Clark"
]

description = \
    """
    Expat library: Fast streaming XML parser written in C99; migrated from SourceForge to GitHub.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
]

variants = [
    ["platform-linux"],
]

tools = [
    "xmlwf",
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "expat-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")

    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.EXPAT_INCLUDE_PATH.set("{root}/include")
    env.EXPAT_LIBRARY_PATH.set("{root}/lib")
