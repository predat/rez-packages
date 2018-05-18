name = "ffmpeg"
version = "3.4.2"
authors = ["Fabrice Bellard"]
description = \
    """
    A complete, cross-platform solution to record,
    convert and stream audio and video.
    """
build_requires = []
requires = []
variants = [["platform-linux", "arch-x86_64"]]
tools = ["ffmpeg", "ffprobe", "ffserver"]

uuid = "repository.ffmpeg"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
