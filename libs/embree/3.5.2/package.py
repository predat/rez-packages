# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-glfw

name = "embree"

version = "3.5.2"

authors = [
    "Intel Embree development team."
]

description = \
    """
    Intel® Embree is a collection of high performance ray tracing kernels that
    helps graphics application engineers to improve the performance of their photorealistic rendering application.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "tbb-2017.U6+",
    "glfw-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "embree-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    env.CMAKE_MODULE_PATH.prepend("{root}/")

    # Helper environment variables.
    env.EMBREE_BINARY_PATH.set("{root}/bin")
    env.EMBREE_INCLUDE_PATH.set("{root}/include")
    env.EMBREE_LIBRARY_PATH.set("{root}/lib64")

