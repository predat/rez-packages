name = "boost"

version = "1.66.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

private_build_requires = ["python-2.7", "gcc-6.3.1"]

variants = [["platform-linux"]]

uuid = "repository.boost"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    # cmake FindPackage env vars
    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
