# Taken from OSS-Pipeline from  https://github.com/OSS-Pipeline/rez-openvdb

name = "openvdb"

version = "5.2.0"

authors = [
    "Ken Museth",
    "Peter Cucka",
    "Mihai Aldén",
    "David Hill",
    "DreamWorks Animation"
]

description = \
    """
    OpenVDB is an Academy Award-winning open-source C++ library comprising a novel hierarchical data structure and a
    suite of tools for the efficient storage and manipulation of sparse volumetric data discretized on
    three-dimensional grids.
    """

requires = [
    "platform-linux",
    "blosc-1.5+",
    "boost-1.6+",
    "cmake-3+",
    "gcc-6+",
    "glfw-3+",
    "ilmbase-2.2.1+<2.4",
    "openexr-2.2.1+<2.4",
    "tbb-2017.U6+",
    "zlib-1.2+"
]

variants = [
    #  ["python-2.7"],
    ["python-3.6"]
]

tools = [
    "vdb_print",
    "vdb_render",
    "vdb_view"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "openvdb-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION))

    # Helper environment variables.
    env.OPENVDB_BINARY_PATH.set("{root}/bin")
    env.OPENVDB_INCLUDE_PATH.set("{root}/include")
    env.OPENVDB_LIBRARY_PATH.set("{root}/lib")
