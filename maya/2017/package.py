name = "maya"
version = "2017.0.60" # from mayapy -c "import maya.standalone; maya.standalone.initialize(name='python'); print maya.cmds.about(api=True); maya.standalone.uninitialize()"
authors = ["Autodesk"]
description = "Autodesk maya 2017 Update 4"
build_requires = []
variants = [["platform-linux", "arch-x86_64"]]

tools = ["maya", "mayapy"]

uuid = "repository.maya"


def commands():
#    #source("/opt/rez/completion/complete.sh")
#
#    # in order to avoid maya 2014-x64/prefs/shelves/shelf_Polygons.mel Syntax error
#    env.LC_NUMERIC="C"
#    env.AUTODESK_ADLM_THINCLIENT_ENV="/prod/apps/{this.name}/common/AdlmThinClientCustomEnv.xml"
#    env.MAYA_LICENSE="unlimited"
#    env.MAYA_LICENSE_METHOD="network"
#    # Disable Autodesk Customer Involvement Program (CIP)
#    env.MAYA_DISABLE_CIP="1"
#    # Disable Customer Error Reporting (CER)
#    env.MAYA_DISABLE_CER="1"
#
#    # When Maya encounters a fatal error, this variable writes a crash
#    # report file (MayaCrashLog[yymmdd.hhmm].log) to the directory specified
#    # with the TMP environment variable. This file contains a detailed
#    # description of what Maya was doing when the failure occurred.
#    # To enable this option, set the value equal to 1.
#    # To disable it, set the value to 0 (zero) or leave it undefined.
#    # (Windows and Linux)
#    env.MAYA_DEBUG_ENABLE_CRASH_REPORTING="0"
#
#    # Use this environment variable to help ensure that pop-up windows are
#    # raised to the top of the list when using Gnome desktop
#    # (metacity window manager).
#    env.MAYA_FORCE_SHOW_ACTIVATE="1"
#
#    #env.PATH.append("{root}/bin")
#    env.PATH.append("/prod/apps/{this.name}/{version}/{system.platform}/bin/")
#
#    env.PYTHONPATH.append(
#        env.PP_SOFTWARE_APP.value() + "/{this.name}/{version}/{system.platform}/lib/python2.7/site-packages")
#
#    env.LD_LIBRARY_PATH.append("/prod/apps/{this.name}/{version}/{system.platform}/lib")
#
#
#
#    if building:
#        #env.PYTHON_INCLUDE_DIR = "{root}/include/python2.7"
#        # only used to see libpythonX.X.a file
#        env.LD_LIBRARY_PATH.append("{root}/lib")
#        env.MAYA_LOCATION.append("{root}")
    env.MAYA_LOCATION.set("{root}/maya")
    env.PATH.prepend("{root}/maya/bin")
    env.PATH.prepend("{root}/bin")

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")

    env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    env.MAYA_VERSION = 2017.0

    #only need by version < 2017
    # env.MAYA_VP2_USE_GPU_MAX_TARGET_SIZE = 1
