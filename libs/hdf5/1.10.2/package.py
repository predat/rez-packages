name = "hdf5"

version = "1.10.2"

authors = [
    "The HDF Group"
]

description = \
    """
    Data model, library, and file format for storing and managing data.
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64"]
]

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
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.HDF5_INCLUDE_DIR = "{root}/include"
        # static libs
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
