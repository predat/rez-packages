Overview
========

This is a repository of package installers. Each directory contains a rez
project that you can build (using `rez-build`) or release (using `rez-release`).
Doing so will build or release the associated software (gcc, boost etc) as a
rez package. See the following [Quick Start Guide](https://github.com/nerdvegas/rez/wiki/Getting-Started) for more details.

Please note that this project repository is for reference only. You should copy
them into your own repo - at that point you can set the correct versions, put a
requirement on your operating system of choice, and so on.


Quick Start Guide
-----------------

1.  Copy contents of ./repository to another location;

2.  Optionally (if you want to release packages) put this copy under version control;

3.  Cd into a package you would like to install (eg hello_world_py/1.0.0);

4.  Make any necessary changes to the package.py and/or CMakeLists.txt file. A
    package's definition and/or build process will often not be exactly what a
    studio wants.

5.  Run:

    ```bash
    $ rez-build -i
    ```

    This will build the package, and install it to your local packages path,
    typically ~/packages.

    You often need to provide the source archive that the packages is built
    from. Rez looks for such archives under the path set by the environment
    variable REZ_REPO_PAYLOAD_DIR. If not set, an error message will tell you.
    Set this variable and goto the next step.

    If the source archive you need is not present under REZ_REPO_PAYLOAD_DIR,
    an error message will tell you so. Download the archive from the suggested
    URL, and goto the next step.

6.  Test:

    ```bash
    $ rez-env hello_world_py
    $ hello
    Hello world!
    ```

7.  Once your local install is working, you may want to release the package so
    the whole studio can use it. To release:

    ```bash
    $ rez-release
    ```

8.  That's it. To install newer versions, download the newer source archives,
    update package.py/CMakeLists.txt appropriately, and rez-release once more.
    All changes to your installer scripts are now kept in rez packages, and are
    under source control.

