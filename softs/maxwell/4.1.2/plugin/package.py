name = "maxwell_plugin"
version = "4.1.2"
authors = [""]
description = ""
plugin_for = ["maya"]
variants = [
    ["maya-2017"]
]

build_requires = []
requires = ["maxwell"]
tools = []

uuid = "repository.maxwell_plugin"

def commands():
    env.MAYA_PLUG_IN_PATH.append("{root}/maxwell/bin/plug-ins")
    env.MAYA_SCRIPT_PATH.append("{root}/maxwell/scripts/AETemplates")
    env.MAYA_SCRIPT_PATH.append("{root}/maxwell/scripts/others")
    env.XBMLANGPATH.append("{root}/maxwell/icons/%B")
    env.MAYA_RENDER_DESC_PATH.append("{root}/maxwell/bin/rendererDesc")
