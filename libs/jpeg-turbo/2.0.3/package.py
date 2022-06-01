# Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-jpeg-turbo

name = "jpeg_turbo"

version = "2.0.3"

authors = [
    "libjpeg-turbo Development Team"
]

description = \
    """
    libjpeg-turbo is a JPEG image codec that uses SIMD instructions (MMX, SSE2, AVX2, NEON, AltiVec) to accelerate
    baseline JPEG compression and decompression on x86, x86-64, ARM, and PowerPC systems, as well as progressive
    JPEG compression on x86 and x86-64 systems.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "yasm-1+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "cjpeg",
    "djpeg",
    "jpegtran",
    "rdjpgcom",
    "tjbench",
    "wrjpgcom"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "jpeg_turbo-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.JPEG_TURBO_BINARY_PATH.set("{root}/bin")
    env.JPEG_TURBO_INCLUDE_PATH.set("{root}/include")
    env.JPEG_TURBO_LIBRARY_PATH.set("{root}/lib")
