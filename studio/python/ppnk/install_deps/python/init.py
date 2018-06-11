# -*- coding: utf-8 -*-

import os
import sys
import nuke
import logging

# loggger
# =======================================================================
format = '%(asctime)s %(levelname)s\t%(module)s.%(funcName)s | %(message)s'
logging.basicConfig(format=format)
logger = logging.getLogger('init')
logger.setLevel(logging.INFO)

# add subfolder in plugin path
sub_folders = ['./icons', './gizmos', './python', './tcl']
for sub_folder in sub_folders:
    logger.info("Add {sub_folder} to plugin_path".format(sub_folder=sub_folder))
    nuke.pluginAddPath(sub_folder)

# Add the "Fix Studio" menu as the last in nuke.pluginPath() to let it be
# configured first. This is because NUKE initialization scripts are run in
# reverse order of the NUKE plug-in path.
# See http://docs.thefoundry.co.uk/nuke/90/pythondevguide/startup.html#evaluation-order
nuke.pluginAppendPath(os.path.join(os.path.dirname(__file__), './fixstudiomenu'))

# Project Settings > Default format: HD 1920x1080
nuke.knobDefault('Root.format', '1920 1080 1')

# Project Settings > FPS: 25
nuke.knobDefault('Root.fps', '25')


# Shotgun SgTk Nuke Render Farm Integration
# See https://support.shotgunsoftware.com/entries/95440797-Write-Node#Render%20Farm%20Integration%201
def init_sgtk():
    """
    Minimal setup to ensure the tk-nuke engine is up and running
    started outside of the Tank command or Shotgun context menus.
    """

    # Check that we need to start the engine:
    if "TANK_ENGINE" in os.environ:
        # tk-nuke engine is going to be set up by
        # tk-multi-launchapp so we don't need to bother
        return

    # Check that the engine isn't already running
    if "TANK_NUKE_ENGINE_MOD_PATH" in os.environ:
        # tk-nuke engine is running which will handle all
        # engine & context management from now on
        return

    # initialize tk-nuke engine:
    try:
        # Determine the work area path that will be used to
        # create the initial context the engine will be
        # started with.
        for arg in sys.argv:
            if arg.endswith(".nk"):
                # file path was passed through the command line
                nuke_script_path = arg
                # we use the first nuke script provided to determine the project
                break

        if 'nuke_script_path' in locals():
            import sgtk
            # instantiate an sgtk instance from the current work area path:
            tk = sgtk.sgtk_from_path(nuke_script_path)
            # make sure we have synchronised the file system structure from
            # Shotgun (for core v0.15 and above):
            tk.synchronize_filesystem_structure()

            # get ctx based on nuke path
            ctx = tk.context_from_path(nuke_script_path)

            # get template fields
            t_fields = {}
            try:
                # get fields from path
                t = tk.template_from_path(nuke_script_path)
                t_fields = t.get_fields(nuke_script_path)
            except Exception:
                pass

            if t_fields.get("Task") and ctx.entity:
                # get task id from sg
                sg_task = tk.shotgun.find_one("Task", [["content", "is", t_fields.get("Task")], ["entity", "is", ctx.entity]])

                # build a context from the work area path:
                task_ctx = tk.context_from_entity("Task", sg_task.get("id"))

                # Finally, attempt to start the engine for this context:
                logger.info("Init Engine for context : {project}, {entity}, {step}, {task}".format(project=task_ctx.project.get("name"), entity=task_ctx.entity.get("name"), step=task_ctx.step.get("name"), task=task_ctx.task.get("name")))
                sgtk.platform.start_engine("tk-nuke", tk, task_ctx)
    except Exception, e:
        print "Failed to start Toolkit Engine - %s" % e


# ---
# execute function each time nuke start
logger.info('init_sgtk')
init_sgtk()

# execute pp init nuke script
import ppnk.action.ppInitNuke
ppnk.action.ppInitNuke.init_script()

# import cryptomatte_utilities
# cryptomatte_utilities.setup_cryptomatte()
