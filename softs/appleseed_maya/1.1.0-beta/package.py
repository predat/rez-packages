# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "appleseed_maya"

version = "1.1.0-beta"

authors = []

description = ''

requires = [
    'openexr',
    'appleseed']

build_requires = [
    'openexr',
    'oiio',
    'osl',
]

plugin_for = ['maya']

variants = [
    # ["platform-linux", "arch-x86_64", "maya-2016.0"],
    ["platform-linux", "arch-x86_64", "maya-2016.5"],
    ["platform-linux", "arch-x86_64", "maya-2017.0"],
    ["platform-linux", "arch-x86_64", "maya-2018.0"],
]

uuid = "repository.appleseed_maya"


def commands():

    env.MAYA_MODULE_PATH.append("{root}")

    env.APPLESEED_SEARCHPATH.append("$APPLESEED/shaders/maya")
    env.APPLESEED_SEARCHPATH.append("$APPLESEED/shaders/appleseed")

    env.MAYA_RENDER_DESC_PATH.append("{root}/renderDesc")
    env.MAYA_PRESET_PATH.append("{root}/presets")
    env.MAYA_CUSTOM_TEMPLATE_PATH.append("{root}/scripts/appleseedMaya/AETemplates")
    env.MAYA_SHELF_PATH.append("{root}/prefs/shelves")

    # env.MAYA_DEBUG_NO_SIGNAL_HANDLERS.set("1")
    # env.APPLESEED_MAYA_LOG_LEVEL.set("debug")
