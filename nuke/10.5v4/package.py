name = "nuke"

version = "10.5v4"
short_version = version.split('v')[0]


authors = [
    "The Foundry"
]

description = \
    """
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]


uuid = "repository.nuke"

def commands():

    env.PATH.append("/prod/apps/nuke/{version}/linux")
    env.foundry_LICENSE = "4101@licfoundry.prs.vfx.int"
    env.FN_DISABLE_LICENSE_DIALOG = "1"

    alias('nuke', 'Nuke10.5')


    if building:
        env.LD_LIBRARY_PATH.append("{root}/lib")
        env.Nuke_ROOT.append("/prod/apps/nuke/{version}/linux")

