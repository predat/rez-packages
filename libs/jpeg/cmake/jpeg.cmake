find_package(JPEG)
set(jpeg_INCLUDE_DIRS ${JPEG_INCLUDE_DIR})
get_filename_component(jpeg_LIBRARY_DIRS ${JPEG_LIBRARY} PATH)
set(jpeg_LIBRARIES ${JPEG_LIBRARY})
