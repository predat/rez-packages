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

    # Shotgun
    env.PP_SHOTGUN = env.PP_ROOT_DIR.value() + '/shotgun'

    # source("/opt/rez/completion/complete.sh")

    env.PATH.append('{root}/bin')
