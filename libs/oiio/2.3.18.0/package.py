# From OSS-Pipeline from https://github.com/OSS-Pipeline/rez-oiio
name = "oiio"

version = "2.3.18.0"

authors = [
    "Sony Pictures Imageworks"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related classes, utilities, and
    applications. There is a particular emphasis on formats and functionality used in professional, large-scale
    animation and visual effects work for film. OpenImageIO is used extensively in animation and VFX studios all
    over the world, and is also incorporated into several commercial products.
    """

requires = [
    "boost-1.61+",
    "cmake-3.12+",
    "gcc-6+",
    "glew-2+",
    "imath-2.3+",
    "jpeg_turbo-2+",
    #  "numpy-1.12+",
    "ocio-1.1+",
    "openexr-2.3+",
    "openjpeg-2+",
    "png-1.6+",
    "pugixml-1+",
    #  "pybind11-2.2+",
    "tbb-2018+",
    "tiff-4+",
    "zlib-1.2+",
    "ptex-2.3.1+",
    #  "python-3.7+",
]

variants = [
    ["platform-linux"]
]

tools = [
    "iconvert",
    "idiff",
    "igrep",
    "iinfo",
    "maketx",
    "oiiotool"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "oiio-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib64/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")
    env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")

    # Helper environment variables.
    env.OIIO_BINARY_PATH.set("{root}/bin")
    env.OIIO_INCLUDE_PATH.set("{root}/include")
    env.OIIO_LIBRARY_PATH.set("{root}/lib64")
    env.OIIO_LIBRARY_PATH.set("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append('{root}')
