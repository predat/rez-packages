# From OSS-Pipeline from https://github.com/OSS-Pipeline/rez-openjpeg

name = "openjpeg"

version = "2.3.1"

authors = [
    "Image and Signal Processing Group, UCL"
]

description = \
    """
    OpenJPEG is an open-source JPEG 2000 codec written in C language. It has been developed in order to promote the
    use of JPEG 2000, a still-image compression standard from the Joint Photographic Experts Group.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "png-1.6+",
    "tiff-4+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "opj_compress",
    "opj_decompress",
    "opj_dump"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "openjpeg-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
    # We know that the version numbers are separated by a ".", so we should safely be able to get the
    # number we want through a split.
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/openjpeg-" + str(version).split(".")[0] + "." + str(version).split(".")[1])

    # Helper environment variables.
    env.OPENJPEG_BINARY_PATH.set("{root}/bin")
    env.OPENJPEG_INCLUDE_PATH.set("{root}/include")
    env.OPENJPEG_LIBRARY_PATH.set("{root}/lib")
