# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope, early, resolve  # make linter happy


name = "xerces"

version = "3.1.2"

authors = [
]

description = \
    """
Xerces-C++ is a validating XML parser written in a portable subset of C++. Xerces-C++ makes it easy to give your application the ability to read and write XML data. A shared library is provided for parsing, generating, manipulating, and validating XML documents using the DOM, SAX, and SAX2 APIs.
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64"]
]

tools = []

uuid = "repository.xerces"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
