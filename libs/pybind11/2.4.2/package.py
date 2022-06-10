name = "pybind11"

version = "2.4.2"

authors = [
    "Wenzel Jakob"
]

description = \
    """
    pybind11 is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create
    Python bindings of existing C++ code.
    """

requires = [
    "platform-linux",
    "cmake-3+",
    "gcc-6+",
]

variants = [
    ["python-2.7"],
    ["python-3.6"]
]

tools = [
    ""
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pybind11-{version}".format(version=str(version))

def commands():
    env.CMAKE_MODULE_PATH.prepend("{root}/share/cmake/pybind11")

    # Helper environment variables.
    env.PYBIND11_INCLUDE_PATH.set("{root}/include")
