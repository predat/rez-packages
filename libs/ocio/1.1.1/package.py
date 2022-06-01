name = "ocio"

version = "1.1.1"

authors = [
    "Sony Pictures Imageworks"
]

description = \
    """
    OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production with an
    emphasis on visual effects and computer animation. OCIO provides a straightforward and consistent user experience
    across all supporting applications while allowing for sophisticated back-end configuration options suitable for
    high-end production usage. OCIO is compatible with the Academy Color Encoding Specification (ACES) and is
    LUT-format agnostic, supporting many popular formats.
    """

requires = [
    "boost-1.61+",
    "cmake-3+",
    "gcc-6+",
    "yaml_cpp-0.6+",
    "tinyxml-2.6+",
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "ocio-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    #  env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
    env.CMAKE_MODULE_PATH.prepend("{root}:{root}/cmake")

    # Helper environment variables.
    env.OCIO_BINARY_PATH.set("{root}/bin")
    env.OCIO_INCLUDE_PATH.set("{root}/include")
    env.OCIO_LIBRARY_PATH.set("{root}/lib")
