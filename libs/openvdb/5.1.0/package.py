# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "openvdb"

version = "5.1.0"

authors = [
    "Dreamwork Animation"
]

description = \
    """
    OpenVDB is an open source C++ library comprising a novel hierarchical
    data structure and a large suite of tools for the efficient storage
    and manipulation of sparse volumetric data discretized on
    three-dimensional grids. It is developed and maintained by
    DreamWorks Animation for use in volumetric applications typically
    encountered in feature film production.
    """

requires = [
    "blosc-1.11",
    "openexr-2.2",
    "boost-1.61",
    "tbb-4.4"
]

build_requires = [
    # "cppunit",
    "glfw-3.2"
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

tools = [
    "vdb_print",
    "vdb_render",
    "vdb_view"
]

uuid = "repository.openvdb"


def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append("{root}/lib/python2.7")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
