#Taken from OSS-Pipeline from https://github.com/OSS-Pipeline/rez-markupsafe

name = "markupsafe"

version = "1.1.1"

authors = [
    "Armin Ronacher"
]

description = \
    """
    Safely add untrusted strings to HTML/XML markup.
    """

requires = [
    "platform-linux",
    "cmake-3+",
]

variants = [
    ["python-2.7"],
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "markupsafe-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
