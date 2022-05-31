# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-bison

name = "bison"

version = "3.4"

authors = [
    "GNU"
]

description = \
    """
    Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic
    LR or generalized LR (GLR) parser employing LALR(1) parser tables.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "bison",
    "yacc"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "bison-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.BISON_BINARY_PATH.set("{root}/bin")
    env.BISON_LIBRARY_PATH.set("{root}/lib")
