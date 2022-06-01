# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-glew

name = "glew"

version = "2.1.0"

authors = [
    "Milan Ikits",
    "Marcelo Magallon",
    "Nigel Stewart"
]

description = \
    """
    The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++ extension loading library.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "glewinfo",
    "visualinfo"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "glew-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PKG_CONFIG_PATH.prepend("{root}/lib64/pkgconfig")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib64/cmake/glew")

    # Helper environment variables.
    env.GLEW_BINARY_PATH.set("{root}/bin")
    env.GLEW_INCLUDE_PATH.set("{root}/include")
    env.GLEW_LIBRARY_PATH.set("{root}/lib64")
