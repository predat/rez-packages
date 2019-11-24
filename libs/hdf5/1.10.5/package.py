name = "hdf5"

version = "1.10.5"

authors = [
    "The HDF Group"
]

description = \
    """
    Data model, library, and file format for storing and managing data.
    """

private_build_requires = ['gcc-6.3.1']

variants = [["platform-linux"]]

tools = [
    "gif2h5"
    "h52gif"
    "h5cc"
    "h5copy"
    "h5debug"
    "h5diff"
    "h5dump"
    "h5import"
    "h5jam"
    "h5ls"
    "h5mkgrp"
    "h5perf_serial"
    "h5redeploy"
    "h5repack"
    "h5repart"
    "h5stat"
    "h5unjam"
]

uuid = "repository.hdf5"

def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.HDF5_INCLUDE_DIR = "{root}/include"
        # static libs
        env.CMAKE_PREFIX_PATH.append("{root}")
        env.LD_LIBRARY_PATH.append("{root}/lib")
