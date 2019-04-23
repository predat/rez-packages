# -*- coding: utf-8 -*-

import os

name = 'cookiecutter'

version = '1.6.0'

tools = ['cookiecutter']

build_requires = ["setuptools"]

variants = [["platform-linux", "arch-x86_64", "python-2.7"]]

# Install into a specific location
with scope("config"):
    release_packages_path = "/s/apps/packages/dev"

custom = \
    {
        'amailRecipients': ['mian_pkg_announcement@mikrosimage.eu'],
        'authors': ['Audrey Roy Greenfeld'],
        'description': 'A command-line utility that creates projects from cookiecutters (project templates). E.g. Python package projects, jQuery plugin projects.',
        'doc': '',
        'git': 'https://github.com/audreyr/cookiecutter',
        'wiki': 'https://cookiecutter.readthedocs.io/en/latest/'
    }

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.cookiecutter'
