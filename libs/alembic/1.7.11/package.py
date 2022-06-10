# From OSS-Pipeline from https://github.com/OSS-Pipeline/rez-alembic

name = "alembic"

version = "1.7.11"

authors = [
    "Sony Pictures Imageworks"
]

description = \
    """
    Alembic is an open framework for storing and sharing scene data that includes a C++ library, a file format,
    and client plugins and applications.
    """

requires = [
    "platform-linux",
    "boost-1.61+",
    "cmake-3+",
    "gcc-6+",
    "ilmbase-2.2.1<2.4",
    "pyilmbase-2.2.1<2.4",
]

variants = [
    ["python-2.7"]
]

tools = [
    "abcdiff",
    "abcecho",
    "abcechobounds",
    "abcls",
    "abcstitcher",
    "abctree"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "alembic-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/Alembic")

    # Helper environment variables.
    env.ALEMBIC_BINARY_PATH.set("{root}/bin")
    env.ALEMBIC_INCLUDE_PATH.set("{root}/include")
    env.ALEMBIC_LIBRARY_PATH.set("{root}/lib")
