name = "sgtk"
authors = ["Sylvain Maziere"]
description ="Sgtk config"
build_requires = []
variants = []
uuid = "repository.sgtk"
build_command = "python {root}/install.py"
__version = "1.0.0"


@early()
def version():
    return this.__version + '-dev'


@early()
def tools():
    return ['tank']


def commands():

    env.PYTHONPATH.prepend( env.PP_SGTK_HOME.value() + '/install/core/python')
    env.PATH.append( env.PP_SGTK_HOME.value() )
