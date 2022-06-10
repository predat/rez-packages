name = "jinja2"

version = "2.10.1"

authors = [
    "Armin Ronacher"
]

description = \
    """
    A small but fast and easy to use stand-alone template engine written in pure python.
    """

requires = [
    "cmake-3+",
    "markupsafe-1.1+",
    "python-2.7+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "jinja2-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
