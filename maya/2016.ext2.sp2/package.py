name = "maya"

version = "2016.ext2.sp2"

authors = [
    "Autodesk"
]

description = \
    """
    Autodesk maya 2016 Extension 2 Service Pack 2
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64"]
]


uuid = "repository.maya"

def commands():
    #source("/opt/rez/completion/complete.sh")

    # in order to avoid maya 2014-x64/prefs/shelves/shelf_Polygons.mel Syntax error
    env.LC_NUMERIC="C"
    env.AUTODESK_ADLM_THINCLIENT_ENV="/prod/softprod/apps/maya/common/AdlmThinClientCustomEnv.xml"
    env.MAYA_LICENSE="unlimited"
    env.MAYA_LICENSE_METHOD="network"
    # Disable Autodesk Customer Involvement Program (CIP)
    env.MAYA_DISABLE_CIP="1"
    # Disable Customer Error Reporting (CER)
    env.MAYA_DISABLE_CER="1"

    # When Maya encounters a fatal error, this variable writes a crash
    # report file (MayaCrashLog[yymmdd.hhmm].log) to the directory specified
    # with the TMP environment variable. This file contains a detailed
    # description of what Maya was doing when the failure occurred.
    # To enable this option, set the value equal to 1.
    # To disable it, set the value to 0 (zero) or leave it undefined.
    # (Windows and Linux)
    env.MAYA_DEBUG_ENABLE_CRASH_REPORTING="0"

    # Use this environment variable to help ensure that pop-up windows are
    # raised to the top of the list when using Gnome desktop
    # (metacity window manager).
    env.MAYA_FORCE_SHOW_ACTIVATE="1"

    env.PATH.append("{root}/bin")
    env.PATH.append("/prod/softprod/apps/maya/2016.ext2.sp2/linux/bin/")
    #env.PATH.append("/opt/rez/bin/rez")
    #env.PYTHONPATH.append("{root}/lib/python2.7")


    if building:
        #env.PYTHON_INCLUDE_DIR = "{root}/include/python2.7"
        # only used to see libpythonX.X.a file
        env.LD_LIBRARY_PATH.append("{root}/lib")
        env.MAYA_LOCATION.append("/prod/softprod/apps/maya/2016.ext2.sp2/linux")

