FIND_PACKAGE(Qt4 REQUIRED)
INCLUDE(${QT_USE_FILE})

get_cmake_property(_variableNames VARIABLES)
foreach (_variableName ${_variableNames})
    message(STATUS "${_variableName}=${${_variableName}}")
endforeach()

set(qt_INCLUDE_DIRS     ${QT_INCLUDE_DIR})
set(qt_LIBRARY_DIRS   	${QT_LIBRARY_DIR})
set(qt_LIBRARIES ${QT_LIBRARIES})
