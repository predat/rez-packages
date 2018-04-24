name = "nuke"
version = "10.0v6"
version_short = version.split('v')[0]

authors = ["The Foundry"]
description = """ """
build_requires = []
variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.nuke"

def commands():
    #env.PATH.append("/prod/apps/nuke/{version}/linux")
    env.foundry_LICENSE.append("4101@licfoundry.prs.vfx.int")
    env.FN_DISABLE_LICENSE_DIALOG.append("1")

    import os
    nuke_exe = os.path.join(
        "/prod/apps/",
        str(this.name),
        str(this.version),
        "linux",
        "Nuke" + str(this.version_short))

    alias('nuke', nuke_exe)

    if building:
        #env.LD_LIBRARY_PATH.append("{root}/lib")
        env.Nuke_ROOT.append("/prod/apps/nuke/{version}/linux")

