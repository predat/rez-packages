import os
import shutil
import subprocess


compile_cmd = """/usr/bin/c++ \
  -DUSE_FREETYPE -DUSE_GLEW -DUSE_JPEG_TURBO=1 -DNDEBUG \
  -D__STDC_CONSTANT_MACROS -D__STDC_LIMIT_MACROS -DtxReader_EXPORTS \
  -O3 -fPIC -std=c++11 -msse \
  -I$REZ_OIIO_ROOT/include/OpenImageIO \
  -I$REZ_OIIO_ROOT/include \
  -I$REZ_ILMBASE_ROOT/include \
  -I$REZ_OPENEXR_ROOT/include \
  -I$REZ_OPENEXR_ROOT/include/OpenEXR \
  -I$REZ_ILMBASE_ROOT/include/OpenEXR \
  -I$Nuke_ROOT/include \
  -Wall -Werror -fno-math-errno -Wno-error=unused-local-typedefs \
  -Wno-unused-local-typedefs -Wno-unused-result \
  -UUSE_FIELD3D \
  -o {object_file_path} -c {source_file_path}
"""


link_cmd = """/usr/bin/c++ \
  -fPIC -O3 -DNDEBUG -shared -Wl,-soname,{plugin}.so -o {binary_file_path} {object_file_path} \
  -L$Nuke_ROOT -lDDImage \
  -L$REZ_BOOST_ROOT/lib \
  $REZ_OIIO_ROOT/lib/libOpenImageIO.so.1.7.16 \
  $REZ_OPENEXR_ROOT/lib/libIlmImf.so \
  $REZ_ILMBASE_ROOT/lib/libImath.so \
  $REZ_ILMBASE_ROOT/lib/libIex.so \
  $REZ_ILMBASE_ROOT/lib/libHalf.so \
  $REZ_ILMBASE_ROOT/lib/libIlmThread.so \
  $REZ_BOOST_ROOT/lib/libboost_filesystem.so.1.63.0 \
  $REZ_BOOST_ROOT/lib/libboost_regex.so.1.63.0 \
  $REZ_BOOST_ROOT/lib/libboost_system.so.1.63.0 \
  $REZ_BOOST_ROOT/lib/libboost_thread.so.1.63.0 \
  -lpthread -lz -lbz2 -lpng -ljpeg -lopenjpeg -ltiff -lfreetype \
  -lboost_filesystem -lboost_regex -lboost_system -lboost_thread \
  -Wl,-rpath,$Nuke_ROOT:$REZ_ILMBASE_ROOT/lib:$REZ_OPENEXR_ROOT/lib:$REZ_OIIO_ROOT/lib:$REZ_BOOST_ROOT/lib
"""

if __name__ == "__main__":

    archive_path = os.path.join(
            os.environ['REZ_REPO_PAYLOAD_DIR'],
            'oiio',
            'Release-1.7.16.tar.gz')

    src_path = os.path.join(
            os.environ['REZ_BUILD_SOURCE_PATH'],
            'build')

    # extract archive
    cmd = 'tar -zxf %s -C %s' % (archive_path, src_path)
    subprocess.call(cmd, shell=True)


    for plugin in ["txReader", "txWriter"]:

        plugin_path = os.path.join(src_path, "oiio-Release-1.7.16", "src", "nuke", plugin)

        source_file_path = os.path.join(plugin_path, plugin + ".cpp")

        object_file_path = os.path.join(os.environ['REZ_BUILD_PATH'], plugin + ".cpp.o")

        binary_file_path = os.path.join(os.environ['REZ_BUILD_PATH'], plugin + ".so")


        # compile
        cmd = compile_cmd.format(
            source_file_path=source_file_path,
            object_file_path=object_file_path)
        subprocess.call(cmd, shell=True)


        # link
        cmd = link_cmd.format(
            object_file_path=object_file_path,
            binary_file_path=binary_file_path,
            plugin=plugin)
        print cmd
        subprocess.call(cmd, shell=True)


        # install
        if not os.path.exists(os.environ['REZ_BUILD_INSTALL_PATH']):
            os.makedirs(os.environ['REZ_BUILD_INSTALL_PATH'])

        shutil.copyfile(
            binary_file_path,
            os.path.join(
                os.environ['REZ_BUILD_INSTALL_PATH'],
                plugin + ".so")
        )

    #from pprint import pprint
    #for k, v in os.environ.items():
    #    if 'INSTALL' in k:
    #        print "%s=%s" %(k, v)

