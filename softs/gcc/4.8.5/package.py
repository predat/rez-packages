name = "gcc"

version = "4.8.5"

authors = [
    "GNU"
]

description = \
    """
    GNU project C and C++ compiler.
    """

variants = [
    ["platform-linux", "arch-x86_64","os-CentOS-6.8"],
    ["platform-linux", "arch-x86_64","os-CentOS-7.3.1611"]
]
requires = [ 
    #"binutils-2.25" 
]

tools = [
    "gcc",
    "g++",
    "c++",
    "cpp",
    "gcc-ar",
    "gcc-ranlib",
    "gfortran",
    "gcc-nm",
    "gcov"
]

uuid = "repository.gcc"

def commands():
    pass
