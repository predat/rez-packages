name = "mentalray"
version = "2016.5.0-1902"
version_short = version.split('v')[0]

authors = ["NVidia"]
description =  """ """
build_requires = []
variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.mentalray"


plugin_for = ['maya']


def commands():

    app_location = "/prod/apps/mental_ray"
    env.MAYA_MODULE_PATH.append("/prod/apps/mental_ray/{version}/linux/modules/maya/2016.5")
    env.MAYA_PLUG_IN_PATH.append("/prod/apps/mental_ray/{version}/linux/mentalrayForMaya2016.5/plug-ins")
    env.MAYA_SCRIPT_PATH.append(("/prod/apps/mental_ray/{version}/linux/mentalrayForMaya2016.5/scripts"))
    env.MAYA_PRESET_PATH.append("/prod/apps/mental_ray/{version}/linux/mentalrayForMaya2016.5/presets")
    env.XBMLANGPATH.append("/prod/apps/mental_ray/{version}/linux/mentalrayForMaya2016.5/%B")

