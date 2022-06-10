# Taken from OSS-Pipeline form https://github.com/OSS-Pipeline/rez-pyopengl

name = "pyopengl"

version = "3.1.0"

authors = [
    "Mike C. Fletcher"
]

description = \
    """
    Standard OpenGL bindings for Python.
    """

requires = [
    "cmake-3+",
    "platform-linux"
]

variants = [
    ["python-2.7"],
    ["python-3.6"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pyopengl-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
