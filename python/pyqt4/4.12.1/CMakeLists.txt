CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


rez_find_packages(PREFIX pkgs AUTO)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-${version}/PyQt4_gpl_x11-${version}.tar.gz)


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND sh -c "python configure.py --confirm-license --verbose \
    -b ${CMAKE_INSTALL_PREFIX}/bin \
    -d ${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages \
    --sipdir ${CMAKE_INSTALL_PREFIX}/share/sip \
    -e QtCore -e QtGui -e QtHelp -e QtMultimedia -e QtNetwork -e QtDeclarative \
    -e QtScript -e QtScriptTools -e QtOpenGL -e QtSvg -e QtSql -e QtTest \
    -e QtWebKit -e QtXml -e QtXmlPatterns -e QtDesigner "
    BUILD_COMMAND make -j12
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND make install
    # ALWAYS 1
)


#rez_install_files(
#    cmake/ocio.cmake
#    DESTINATION .
#)
