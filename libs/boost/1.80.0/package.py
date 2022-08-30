name = "boost"

version = "1.80.0"

authors = [
    "Beman Dawes",
    "David Abrahams"
]

description = \
    """
    Boost is a set of libraries for the C++ programming language that provide support for tasks and structures such
    as linear algebra, pseudorandom number generation, multithreading, image processing, regular expressions,
    and unit testing.
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
    "boost"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "boost-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    env.CMAKE_PREFIX_PATH.prepend("{root}")

    # Helper environment variables.
    env.BOOST_INCLUDE_PATH.set("{root}/include")
    env.BOOST_LIBRARY_PATH.set("{root}/lib")
