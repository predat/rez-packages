name = "boost"

version = "1.70.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

private_build_requires = ["gcc"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3.6"],
]

uuid = "repository.boost"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    # cmake FindPackage env vars
    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
