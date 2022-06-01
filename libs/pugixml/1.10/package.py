# Frome OSS-Pipeline from https://github.com/OSS-Pipeline/rez-pugixml/blob/master/package.py

name = "pugixml"

version = "1.10"

authors = [
    "Arseny Kapoulkine"
]

description = \
    """
    pugixml is a C++ XML processing library, which consists of a DOM-like interface with rich traversal/modification
    capabilities, an extremely fast XML parser which constructs the DOM tree from an XML file/buffer, and an XPath
    1.0 implementation for complex data-driven tree queries. Full Unicode support is also available, with Unicode
    interface variants and conversions between different Unicode encodings (which happen automatically during
    parsing/saving).
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pugixml-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/pugixml")

    # Helper environment variables.
    env.PUGIXML_INCLUDE_PATH.set("{root}/include")
    env.PUGIXML_LIBRARY_PATH.set("{root}/lib")
