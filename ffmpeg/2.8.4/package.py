# from: https://github.com/piratecrew/rez-ffmpeg

name = "ffmpeg"

version = "2.8.4"

description = \
    """
    ffmpeg
    """
tools = [
    "ffmpeg",
    "ffplay",
    "ffprobe",
    "ffserver"
]

variants = [
    ["platform-linux","arch-x86_64"]
]

uuid = "repository.ffmpeg"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
