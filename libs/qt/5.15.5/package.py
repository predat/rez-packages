# Taken from OSS-pipline from https://github.com/OSS-Pipeline/rez-qt/blob/master/package.py

name = "qt"

version = "5.15.5"

authors = [
    "The Qt Company"
]

description = \
    """
    Qt is a free and open-source widget toolkit for creating graphical user interfaces as well as cross-platform
    applications that run on various software and hardware platforms such as Linux, Windows, macOS, Android or
    embedded systems with little or no change in the underlying codebase while still being a native application
    with native capabilities and speed.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "assistant",
    "canbusutil",
    "designer",
    "lconvert",
    "linguist",
    "lrelease",
    "lupdate",
    "moc",
    "pixeltool",
    "qcollectiongenerator",
    "qdbus",
    "qdbuscpp2xml",
    "qdbusviewer",
    "qdbusxml2cpp",
    "qdoc",
    "qgltf",
    "qhelpconverterv",
    "qhelpgenerator",
    "qlalr",
    "qmake",
    "qml",
    "qmleasing",
    "qmlimportscanner",
    "qmllint",
    "qmlmin",
    "qmlplugindump",
    "qmlprofiler",
    "qmlscene",
    "qmltestrunner",
    "qtdiag",
    "qtpaths",
    "qtplugininfo",
    "qtwaylandscanner",
    "rcc",
    "uic",
    "xmlpatterns",
    "xmlpatternsvalidator",
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "qt-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.QT_SELECT.set("5")
    env.QTDIR.set("{root}")
    env.QT_QMAKE_EXECUTABLE.set("{root}/bin/qmake")
    env.QTTOOLDIR.set("{root}/bin")
    env.QT_INCLUDE_DIR.set("{root}/include")
    env.QT_LIB_DIR.set("{root}/lib")
    env.QTLIB.set("{root}/lib")
    env.QT_PLUGIN_PATH.set("{root}/plugins")
    env.QML2_IMPORT_PATH.set("{root}/qml")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
    # We know that the version numbers are separated by a ".", so we should safely be able to get the
    # number we want through a split.
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/Qt" + str(version).split(".")[0])

    # Helper environment variables.
    env.QT_BINARY_PATH.set("{root}/bin")
    env.QT_INCLUDE_PATH.set("{root}/include")
    env.QT_LIBRARY_PATH.set("{root}/lib")
