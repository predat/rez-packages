# From OSS-Pipeline from https://github.com/OSS-Pipeline/rez-yasm

name = "yasm"

version = "1.3.0"

authors = [
    "Peter Johnson",
    "Michael Urman"
]

description = \
    """
    Yasm is a complete rewrite of the NASM assembler under the “new” BSD License.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "vsyasm",
    "yasm",
    "ytasm"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "yasm-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.YASM_BINARY_PATH.set("{root}/bin")
    env.YASM_INCLUDE_PATH.set("{root}/include")
    env.YASM_LIBRARY_PATH.set("{root}/lib")
