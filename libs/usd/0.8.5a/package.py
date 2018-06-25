# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "usd"

version = "0.8.5a"

authors = ['Pixar']

description = \
    """
Universal Scene Description (USD) is an efficient, scalable system for authoring, reading, and streaming time-sampled scene description for interchange between graphics applications.
    """

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]


build_requires = [
    'alembic',
    'hdf5',
    'boost',
    'tbb',
    'openexr',
    'oiio',
    'glew',
    'opensubdiv',
    'Jinja2',
    'oiio',
    'opensubdiv',
    'ptex',
    'maya',
    'PyOpenGL',
    'PySide',
    'PySideTools'
]

requires = [
    'Jinja2',
    'PyOpenGL',
    'PySide'
]

tools = []

uuid = "repository.usd"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")
    env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}")

    if "maya" in resolve:
        env.MAYA_PLUG_IN_PATH.append("{root}/third_party/maya/plugin")
        env.MAYA_SCRIPT_PATH.append("{root}/third_party/maya/share/usd/plugins/usdMaya/resources")
        env.XBMLANGPATH.append("{root}/third_party/maya/share/usd/plugins/usdMaya/resources/%B")
