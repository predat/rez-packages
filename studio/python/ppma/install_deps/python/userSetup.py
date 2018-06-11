# -*- coding: utf-8 -*-

"""
userSetup.py allow the avaibility to source/execute code upon launching maya
"""

import os
import maya.cmds as cmds
import maya.mel as mel
import maya.utils as utils
import logging
import ppma.core.ppMenu as ppMenu
import ppma.core.ppSystem as ppSystem
import ppma.action.ppInitMaya as ppInitMaya

# loggger
# =======================================================================
format = '%(asctime)s %(levelname)s\t%(module)s.%(funcName)s | %(message)s'
logging.basicConfig(format=format)
logger = logging.getLogger('userSetup')
logger.setLevel(logging.DEBUG)


def _log_env_var():
    """This function log via logger some env var for debugging.
    """
    env_vars = [
        "PYMEL_SKIP_MEL_INIT"
    ]
    env_vars.sort()
    logger.info("---")
    logger.info("_log_env_var")
    for e in env_vars:
        # get env var and log
        logger.info("{e} : {v}".format(e=e, v=os.environ.get(e)))


# ---
# log some env var for debug
_log_env_var()


# ---
# set option var
def _set_option_var():
    """
    """
    # inactive render setup #1017
    logger.info("Set Option Var {e} : {v}".format(e="renderSetupEnable", v=0))
    cmds.optionVar(iv=('renderSetupEnable', 0))


_set_option_var()

# ---
# build menu
if not cmds.about(batch=True):
    logger.info("Build Menu")

    # --
    # Disactive Error logging for plugin
    cmds.openMayaPref(errlog=False)

    # source and load menu
    utils.executeDeferred('ppMenu.buildMenu()')

# ---
# force abc plugin load due to issue with abc referencing. shotgun ticket 47334
for plugin in ['AbcImport', 'AbcExport']:
    try:
        cmds.loadPlugin(plugin)
        logger.info("pp - plugin successful loaded: %s" % plugin)
    except:
        logger.warning("pp - can't load plugin: %s" % plugin)

# ---
# do path mapping for multiple os like windows, linux
logger.info("Do Path Mapping")
ppSystem.do_pathMapping()

# ---
# source mel script which override maya, maxwell mel
mel_scripts = ["override_maxwell.mel"]
for mel_script in mel_scripts:
    logger.info('source "{m}"'.format(m=mel_script))
    try:
        mel.eval('source "{m}"'.format(m=mel_script))
    except:
        logger.warning("can't source {m}".format(m=mel_script))

# ---
# get project settings and apply it, like unit, fps, etc..
utils.executeDeferred('ppInitMaya.init_script()')
