# -*- coding: utf-8 -*-

name = 'nasm'

version = '2.14.02'

variants = [['platform-linux']]

authors = ['Simon Tatham', 'Julian Hall']

requires = []

private_build_requires = ['gcc-6.3.1', 'cmake-3']

description = """
The Netwide Assembler, NASM, is an 80x86 and x86-64 assembler designed for portability and modularity. It supports a range of object file formats, including Linux and *BSD a.out, ELF, COFF, Mach-O, 16-bit and 32-bit OBJ (OMF) format, Win32 and Win64. It will also output plain binary files, Intel hex and Motorola S-Record formats. Its syntax is designed to be simple and easy to understand, similar to the syntax in the Intel Software Developer Manual with minimal complexity. It supports all currently known x86 architectural extensions, and has strong support for macros.
"""

tools = ['nasm']

uuid = 'repository.%s' % name


def commands():
    env.PATH.append('{root}/bin')
