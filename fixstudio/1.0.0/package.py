name = "fixstudio"
authors = ["Sylvain Maziere"]
description ="Fixstudio Pipeline"
build_requires = []
variants = []
uuid = "repository.fixstudio"
__version = "1.0.0"

#build_command = "python {root}/install.py"



@early()
def version():
    return this.__version + '-dev'



@early()
def tools():
    return ["pp-go-pipe"]



def commands():

    from rez.system import system

    # TODO: need to be override
    env.PP_SITE = "paris"

    env.PP_OS = system.platform

    if env.PP_OS == "linux":

        env.PP_ROOT_DIR = '/prod'
        env.PP_SEP = ':'
        env.XDG_CACHE_HOME="/var/tmp/xdg-cache-$USER"
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
    env.PP_SOFTWARE_TOOLS= env.PP_SOFTWARE.value() + '/tools'

    # studio
    env.PP_STUDIO_PATH = env.PP_ROOT_DIR.value() + "/studio"
    #
    env.PP_PIPE_PATH = env.PP_STUDIO_PATH.value() + "/pipeline/latest"
    env.PP_PIPE_COMMON_PATH = env.PP_PIPE_PATH.value() + "/common"
    env.PP_PIPE_BIN_PATH =  env.PP_PIPE_COMMON_PATH.value() + "/bin"
    env.PP_PIPE_BOOTSTRAP_PATH = env.PP_PIPE_COMMON_PATH.value() + "/share/bootstrap"
    env.PP_PIPE_CONFIG_PATH = env.PP_PIPE_COMMON_PATH.value() + "/share/config"
    env.PP_PIPE_ICONS = env.PP_PIPE_COMMON_PATH.value() + "/share/icons"
    env.PP_PIPE_SGTK_PATH = env.PP_PIPE_PATH.value() + "/sgtk"
    env.PP_PIPE_LIB_PATH = env.PP_PIPE_COMMON_PATH.value() + "/lib"
    env.PP_PIPE_UI_PATH = env.PP_PIPE_COMMON_PATH.value() + "/ui"


    env.PP_SHOTGUN = env.PP_ROOT_DIR.value() + '/shotgun'
    env.PP_SGTK_HOME = env.PP_SHOTGUN.value() + '/studio'

    #TODO: TD
    #TODO: users

    # PP_COMMON_LIB_PATH=${PP_PIPE_LIB_PATH}${PP_SEP}${PP_TD_LIB_PATH}${PP_SEP}${PP_USER_LIB_PATH}


    #if defined("PP_DEBUG"):
    if defined("PP_DEBUG") and \
            getenv("PP_DEBUG") == "1":
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"
        print "--------------------------------------------------------------"

    print(str(this.root))

    #source("/opt/rez/completion/complete.sh")

    #env.PATH.append("/prod/softprod/apps/maya/2016/linux/bin/")
    #env.PYTHONPATH.append("{root}/lib/python2.7")


    if building:
        #env.PYTHON_INCLUDE_DIR = "{root}/include/python2.7"
        # only used to see libpythonX.X.a file
        #env.LD_LIBRARY_PATH.append("{root}/lib")
        #env.MAYA_LOCATION.append("{root}")
        pass
