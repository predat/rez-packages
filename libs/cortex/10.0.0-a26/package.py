# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "cortex"

version = "10.0.0-a26"

authors = ['Image Engine']

description = \
    """
The Cortex project provides a set of high quality C++ libraries and Python modules tailored for software development in the visual effects industry. Rather than producing end user tools, the project focuses on creating a reusable set of modules of use to TDs and programmers in a broad range of scenarios - allowing them to focus on the more interesting or innovative aspects of development.
"""

variants = [
    ["platform-linux", "arch-x86_64"]
]


build_requires = [
    'alembic',
    'hdf5',
    'blosc',
    'opensubdiv',
    'maya-2018',
    'nuke-10.5',
    'arnold-5',
    'houdini-16.5',
    'scons'
]

requires = [
    'boost-1.56',
    'openexr-2',
    'usd-0.8.5a',
    'blosc',
    'tbb-4.4',
    'oiio-1.8',
    'glew-2',
]

tools = []

uuid = "repository.cortex"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/python")
    # env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}")

    if "maya" in resolve:
        env.MAYA_PLUG_IN_PATH.append("{root}/maya/plugins")
        env.MAYA_SCRIPT_PATH.append("{root}/maya/mel")
        env.XBMLANGPATH.append("{root}/maya/icons/%B")

    if "nuke" in resolve:
        env.NUKE_PATH.append("{root}/nuke/plugins")

    if "arnold" in resolve:
        pass

    if "houdini" in resolve:
        pass
