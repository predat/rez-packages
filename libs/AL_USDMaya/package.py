# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, resolve  # make linter happy


name = "AL_USDMaya"

version = "0.28.1"

authors = [
    'AnimalLogic'
]

description = \
    """
    """

build_requires = [
    'usd',
    'maya',
    'openexr',
    'glew',
    'boost'
]

requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

tools = [
]

uuid = "repository.AL_USDMaya"


def commands():
    env.AL_USDMAYA_LOCATION = "{root}"
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")

    if "maya" in resolve:
        env.MAYA_PLUG_IN_PATH.append("{root}/plugin")
        env.PXR_PLUGINPATH.append("{root}/lib")
        env.MAYA_VP2_DEVICE_OVERRIDE = 'VirtualDeviceGL'
        env.MAYA_VP2_USE_VP1_SELECTION = 1
