name = "jenkinsapi"

version = "0.3.8"

authors = []

description = \
    """
    """

build_requires = ["setuptools", "pip"]

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3"]
]

tools = ["jenkinsapi_version", "jenkins_invoke"]

uuid = "repository.jenkinsapi"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
