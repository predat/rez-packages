# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "openvdb_maya"

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
    "openexr-2.2",
    # "boost-1.61",
    # "maya-2018",
    "openvdb-5"
]

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "maya-2018"],
    ["platform-linux", "arch-x86_64", "maya-2017"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"],

]

tools = []

uuid = "repository.openvdb"


def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append("{root}/lib/python2.7")

    env.MAYA_MODULE_PATH.append("{root}/maya2018")
