# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-ilmbase

name = "imath"

version = "3.1.5"

authors = [
    "Cary Phillips",
    "Industrial Light & Magic"
]

description = \
    """
    Imath is a C++ and python library of 2D and 3D vector, matrix, and math operations for computer graphics.
    """

requires = [
    "cmake-3.12+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "imath-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.IMATH_INCLUDE_PATH.set("{root}/include")
    env.IMATH_LIBRARY_PATH.set("{root}/lib")
    env.IMATH_CONFIG_PATH.set("{root}/lib/cmake/Imath")
