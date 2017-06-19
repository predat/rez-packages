name = 'pip'

version = '9.0.1'

tools = [
    'pip',
]

variants = [
    ["platform-linux", "arch-x86_64", "python-2.7"]
]

requires = [
    'setuptools-36.0.1',
    'python-2.7.12'
]

build_requires = [
    "gcc-4.8.3"
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = '2c43d523-92bb-4f2b-b812-70202f54d3f1'
