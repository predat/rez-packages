name = "ffmpeg"
version = "3.3.3"
authors = [""]
description = """ """
build_requires = [
    "mp3lame",
    "x264",
    "x265"
]

requires = [
    "mp3lame",
    "x264",
    "x265"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = [
    "ffmpeg",
    "ffserver"
]

uuid = "repository.ffmpeg"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    #if building:
    #    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
    #    env.OPENEXR_INCLUDE_DIR = "{root}/include"
