# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = "blenderseed"
version = "0.8.1-beta"
authors = [""]

description = "Appleseed Rendering engine"

requires = [
    "blender",
    "appleseed"
]

build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.blenderseed"

tools = []


def commands():
    env.BLENDER_USER_SCRIPTS.append("{root}")

    # start blender with addon loaded...
    # blender --addons blenderseed --python-expr "import bpy; bpy.context.scene.render.engine = 'APPLESEED_RENDER'"
