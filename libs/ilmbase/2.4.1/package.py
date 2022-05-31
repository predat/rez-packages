name = "ilmbase"

version = "2.4.1"

authors = ["ILM"]

description = \
"""
Utility libraries from ILM used by OpenEXR.
"""

build_requires = []

private_build_requires = ["gcc"]

variants = [["platform-linux"]]

uuid = "repository.ilmbase"


def commands():

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.CMAKE_PREFIX_PATH.append("{root}")
        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")
