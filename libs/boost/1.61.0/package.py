name = "boost"

version = "1.61.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = []

requires = []

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

uuid = "repository.boost"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
        # cmake FindPackage env vars
        env.BOOST_ROOT = "{root}"
        env.BOOST_INCLUDEDIR = "{root}/include"
