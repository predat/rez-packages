# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building, scope  # male linter happy


name = "requests"

version = "2.18.4"

authors = [
    "Kenneth Reitz <me@kennethreitz.org>",
    "Ian Cordasco <graffatcolmingov@gmail.com>",
    "Nate Prewitt <nate.prewitt@gmail.com>"
]

description = ""

requires = ["pip", "python"]

variants = [["platform-linux", "arch-x86_64"]]

tools = []

uuid = "repository.requests"


def commands():
    env.PYTHONPATH.append("{root}/python")
