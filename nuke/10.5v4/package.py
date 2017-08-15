name = "nuke"
version = "10.5v4"
version_short = version.split('v')[0]

authors = ["The Foundry"]
description =  """ """
build_requires = []
variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.nuke"

has_plugins = True


def commands():
    #env.PATH.append("/prod/apps/nuke/{version}/linux")
    env.foundry_LICENSE = "4101@licfoundry.prs.vfx.int"
    env.FN_DISABLE_LICENSE_DIALOG = "1"

    import os
    nuke_exe = os.path.join(
        env.PP_SOFTWARE_APP.value(), #"/prod/apps/",
        str(this.name),
        str(this.version),
        env.PP_OS.value(),
        "Nuke" + str(this.version_short))

    alias('nuke', nuke_exe)

    if building:
        #env.LD_LIBRARY_PATH.append("{root}/lib")
        #env.Nuke_ROOT.append("/prod/apps/nuke/{version}/linux")
        env.Nuke_ROOT.append(
                os.path.join(
                    env.PP_SOFTWARE_APP.value(),
                    str(this.name),
                    str(this.version),
                    env.PP_OS.value()))

