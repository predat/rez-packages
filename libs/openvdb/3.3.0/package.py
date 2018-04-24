name = "openvdb"

version = "3.3.0"

authors = [
    "Dreamwork Animation"
]

description = \
    """
    OpenVDB is an open source C++ library comprising a novel hierarchical
    data structure and a large suite of tools for the efficient storage
    and manipulation of sparse volumetric data discretized on
    three-dimensional grids. It is developed and maintained by
    DreamWorks Animation for use in volumetric applications typically
    encountered in feature film production.
    """

requires = [
]

build_requires = [
    "blosc",
    "boost-1.55",
    "ilmbase-2.20",
    "openexr-2.20"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8"],
    ["platform-linux", "arch-x86_64", "os-CentOS-7.3.1611"],
]

uuid = "repository.blosc"

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")

