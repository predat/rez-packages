name = "maxwell"
version = "4.1.2"
authors = [""]
description = ""
variants = [["platform-linux", "arch-x86_64"]]
build_requires = []
requires = []
tools = [
    "maxwell",
    "mxed",
    "patchelf",
    "mximerge",
    "pymaxwell"

]

uuid = "repository.maxwell"

def commands():
    env.nextlimit_LICENSE = "8053@licmaxwell.prs.vfx.int"

    env.MAXWELL_ROOT = "{root}/maxwell"
    env.MAXWELL4_ROOT = "{root}/maxwell"
    env.MAXWELL4_MATERIALS_DATABASE = "{root}/maxwell/materials database"
    env.MAXWELL_HONOR_UMASK = 1

    env.PATH.append("{root}/maxwell")
    env.LD_LIBRARY_PATH.append("{root}/maxwell")
