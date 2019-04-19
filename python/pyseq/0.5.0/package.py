name = "pyseq"

version = "0.5.0"

authors = [
    "Ryan Galloway"
]

description = \
    """
    python module that finds groups of items that follow a naming
    convention containing a numerical sequence index.
    """

build_requires = ["setuptools", "pip"]
requires = ["python-2.7"]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = ["lss"]

uuid = "repository.pyseq"

def commands():
    env.PYTHONPATH.append("{root}/python")
