name = "boost"

version = "1.55.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.boost"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    if building:
        env.BOOST_INCLUDE_DIR = "{root}/include"
