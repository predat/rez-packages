name = "ocio"

version = "1.0.9"

authors = [
]

description = \
    """
    """

#build_requires = [
#    "python-2.7",
#    "glew-1",
#    "ilmbase-2.2.0",
#    "openexr-2.2.0",
#    "oiio",
#]

requires = [
     "python"
#    "oiio",
#    "glew-1",
#    "boost-1.63",
#    "ilmbase-2.2.0",
#    "openexr-2.2.0",
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "ociobakelut",
    "ociocheck",
    #"ocioconvert",
    #"ociodisplay",
    #"ociolutimage"
]


uuid = "repository.ocio"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")

    if building:
        env.OCIO_INCLUDE_DIR = "{root}/include"
