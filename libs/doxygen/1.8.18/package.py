# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-doxygen

name = "doxygen"

version = "1.8.18"

authors = [
    "Dimitri van Heesch"
]

description = \
    """
    Doxygen is the de facto standard tool for generating documentation from annotated C++ sources, but it also supports
    other popular programming languages such as C, Objective-C, C#, PHP, Java, Python, IDL (Corba, Microsoft, and
    UNO/OpenOffice flavors), Fortran, VHDL, and to some extent D.
    """

requires = [
    "bison-3+",
    "cmake-3+",
    "flex-2+",
    "gcc-6+",
]

variants = [
    #  ["platform-linux", "python-2.7+<3"],
    ["platform-linux", "python-3"]
]

tools = [
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "doxygen-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")

    # Helper environment variables.
    env.DOXYGEN_BINARY_PATH.set("{root}/bin")
