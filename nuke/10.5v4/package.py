name = "nuke"
version = "10.5v4"
version_short = version.split('v')[0]

authors = ["The Foundry"]
description =  """ """
build_requires = []
requires = ['fixstudio']
variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.nuke"

has_plugins = True

tools = ["Nuke"+str(version_short)]


def commands():
    env.foundry_LICENSE = "4101@licfoundry.prs.vfx.int"
    env.FN_DISABLE_LICENSE_DIALOG = "1"

    import os
    nuke_path = os.path.join(
        env.PP_SOFTWARE_APP.value(),
        str(this.name),
        str(this.version),
        env.PP_OS.value()
    )
    env.PATH.append(nuke_path)

    nuke_exe = os.path.join(nuke_path, 'Nuke' + str(this.version_short))

    alias('nuke', nuke_exe)
    alias('nukeassist', nuke_exe + ' -nukeassist')
    alias('nukex', nuke_exe + ' -nukex')
    alias('nukestudio', nuke_exe + ' -studio')


    if building:
        env.Nuke_ROOT.append(nuke_path)

