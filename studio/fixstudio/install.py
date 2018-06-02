import os


if __name__ == "__main__":

    install_path = os.getenv("REZ_BUILD_INSTALL_PATH")

    #install_py_path = os.path.join(install_path, "python")
    #if not os.path.exists(install_py_path):
    #    os.mkdir(install_py_path)

    print("Installation path: %s" % install_path)
