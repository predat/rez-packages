import os
import nuke
import nukescripts
from ppnk.core import ppMenu
import ppnk.tools.ppToolSet
from ppnk.tools import ppAutoSave
from ppnk.tools import ppLoad3dObject

# Nuke preferences > Performance > Caching > auto-localize from: /prod
nuke_preferences = nuke.toNode('preferences')
nuke_preferences['autoLocalCachePath'].setValue('/prod')
nuke_preferences['autoLocalCachePath'].setEnabled(False)

# Nuke preferences > Panels > Node Graph > postage stamp mode: Static frame
nuke_preferences['postage_stamp_mode'].setValue('Static frame')

# Automatically save preferences to a file
# This is mandatory otherwise they are reset whenever the preferences panel
# is opened and closed (by clicking on the "Cancel" button)
# see http://community.thefoundry.co.uk/discussion/post.aspx?f=190&t=102555&p=891628

preferences_code = """Preferences {
 inputs 0
 name Preferences%s
}""" % nuke_preferences.writeKnobs(nuke.WRITE_USER_KNOB_DEFS | nuke.WRITE_NON_DEFAULT_ONLY | nuke.TO_SCRIPT | nuke.TO_VALUE)

prefs_file_ver = str(nuke.NUKE_VERSION_MAJOR) + '.' + str(nuke.NUKE_VERSION_MINOR)
preference_file = os.path.expandvars('$HOME/.nuke/preferences' + prefs_file_ver + '.nk')

f = open(preference_file, 'w')
f.write(preferences_code)
f.close()

# build pp Menu from yaml file
ppMenu.build_menu()

"""
    Create the ppToolSet menu in the left node menu in nuke.
    The .py is in /prod/studio/pipeline/latest/nuke/common/python/ppnk/tools
    And the .png is in /prod/studio/pipeline/latest/nuke/common/fixstudiomenu
"""
toolbar = nuke.menu("Nodes")
ppnk.tools.ppToolSet.createToolsetsMenu(toolbar)


# Add callback
nuke.addAutoSaveFilter(ppAutoSave.onAutoSave)
nuke.addAutoSaveRestoreFilter(ppAutoSave.onAutoSaveRestore)
nuke.addAutoSaveDeleteFilter(ppAutoSave.onAutoSaveDelete)
nukescripts.addDropDataCallback(ppLoad3dObject.onDropDataCallback)

# Project specific
if os.environ.get('TANK_CURRENT_PC'):

    project_path = os.environ.get('TANK_CURRENT_PC').replace('/prod/shotgun', '/prod/project')

    nuke.pluginAddPath(os.path.join(project_path, '0_setup', 'nuke', 'python'))
    nuke.pluginAddPath(os.path.join(project_path, '0_setup', 'nuke', 'gizmos'))

    menu_file = os.path.join(project_path, '0_setup', 'nuke', 'ppMenu.yml')
    ppMenu.build_menu_from_yaml(menu_file)


import SearchReplacePanel

def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()

nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)

