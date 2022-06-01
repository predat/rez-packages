# From OSS-Pipeline from https://github.com/OSS-Pipeline/rez-tiff/blob/master/package.py

name = "tiff"

version = "4.0.10"

authors = [
    "Sam Leffler",
    "Silicon Graphics"
]

description = \
    """
    TIFF Library and Utilities.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "jpeg_turbo-2+",
    "xz-5+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "fax2ps",
    "fax2tiff",
    "pal2rgb",
    "ppm2tiff",
    "raw2tiff",
    "tiff2bw",
    "tiff2pdf",
    "tiff2ps",
    "tiff2rgba",
    "tiffcmp",
    "tiffcp",
    "tiffcrop",
    "tiffdither",
    "tiffdump",
    "tiffgt",
    "tiffinfo",
    "tiffmedian",
    "tiffset",
    "tiffsplit"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "tiff-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.TIFF_BINARY_PATH.set("{root}/bin")
    env.TIFF_INCLUDE_PATH.set("{root}/include")
    env.TIFF_LIBRARY_PATH.set("{root}/lib")
