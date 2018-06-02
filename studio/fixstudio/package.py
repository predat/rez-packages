# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, this, defined, getenv


name = "fixstudio"

authors = ["Fixstudio"]

description = "Fixstudio Pipeline Configuration and variables"

build_requires = []

variants = []

uuid = "repository.fixstudio"

version = "1.0.0"

# build_command = "python {root}/install.py"

tools = []


def commands():

    from rez.system import system

    env.PP_SITE = 'paris'

    env.PP_OS = system.platform

    if env.PP_OS == "linux":
        env.PP_ROOT_DIR = '/prod'
        env.PP_SEP = ':'
        env.XDG_CACHE_HOME = "/var/tmp/xdg-cache-$USER"
        # env.XDG_DATA_DIRS.append()

    elif env.PP_OS == "osx":
        env.PP_ROOT_DIR = '/prod'
        env.PP_SEP = ':'

    elif env.PP_OS == "windows":
        env.PP_ROOT_DIR = 'z:/prod'
        env.PP_SEP = ';'

    env.PP_PS1_ORIG = "$PS1"
    env.PP_SOFTWARE = env.PP_ROOT_DIR.value() + '/softprod'
    env.PP_SOFTWARE_APP = env.PP_SOFTWARE.value() + '/apps'
    env.PP_SOFTWARE_LIB = env.PP_SOFTWARE.value() + '/libs'
    env.PP_SOFTWARE_TOOLS = env.PP_SOFTWARE.value() + '/tools'

    # Shotgun
    env.PP_SHOTGUN = env.PP_ROOT_DIR.value() + '/shotgun'
    env.PP_SGTK_HOME = env.PP_SHOTGUN.value() + '/studio'

    # TODO: TD
    # TODO: users

    # if defined("PP_DEBUG"):
    if defined("PP_DEBUG") and \
            getenv("PP_DEBUG") == "1":
        print "--------------------------------------------------------------"

    print(str(this.root))
    # source("/opt/rez/completion/complete.sh")
