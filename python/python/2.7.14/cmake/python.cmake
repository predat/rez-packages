find_package(Python)
set(python_INCLUDE_DIRS ${PYTHON_INCLUDE_DIRS})
get_filename_component(python_LIBRARY_DIRS ${PYTHON_LIBRARY} PATH)
set(python_LIBRARIES ${PYTHON_LIBRARIES})
