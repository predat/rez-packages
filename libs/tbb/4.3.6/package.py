name = "tbb"

version = "4.3.6"

authors = [
    "Intel"
]

description = \
    """
    Intel Threading Building Blocks.
    """

requires = [
    "gcc-4.8.3"
]

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64","os-CentOS-6.8"]
]

uuid = "repository.tbb"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib/release")

    if building:
        env.TBB_INCLUDE_DIR = "{root}/include"
