
name = 'build'
version = 'debug'

build_command = False

def commands():
    env.CMAKE_BUILD_TYPE = 'DEBUG'
