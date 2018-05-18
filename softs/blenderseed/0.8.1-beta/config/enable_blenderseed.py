# -*- coding: utf-8 -*-

import os
import bpy


bpy.ops.wm.addon_enable(module='blenderseed')
bpy.ops.wm.save_userpref()

addons = bpy.context.user_preferences.addons

if 'blenderseed' in addons.keys():
    if not addons['blenderseed'].preferences.appleseed_binary_directory:
        addons['blenderseed'].preferences.appleseed_binary_directory = os.path.join(
            os.environ['REZ_APPLESEED_ROOT'], 'bin')
