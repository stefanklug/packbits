#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension

import sys

for cmd in ('egg_info', 'develop'):
    if cmd in sys.argv:
        from setuptools import setup

setup_args = dict(
    name = 'packbits',
    version = '0.5',
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://github.com/kmike/packbits',

    description = 'PackBits encoder/decoder',
    long_description = open('README.rst').read(),
    license = 'MIT License',

    package_dir = {'': 'src'},
    py_modules = ['packbits'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

setup(**setup_args)

## ========== make extension optional (copied from coverage.py) =========
#
#compile_extension = True
#
#if sys.platform.startswith('java'):
#    # Jython can't compile C extensions
#    compile_extension = False
#
#if '__pypy__' in sys.builtin_module_names:
#    # Cython extensions are slow under PyPy
#    compile_extension = False
#
#if compile_extension:
#    setup_args.update(dict(
#        ext_modules = [
#            Extension("_packbits", sources=["src/_packbits.c"])
#        ],
#    ))
#
## For a variety of reasons, it might not be possible to install the C
## extension.  Try it with, and if it fails, try it without.
#try:
#    setup(**setup_args)
#except:     # pylint: disable=W0702
#    # When setup() can't compile, it tries to exit.  We'll catch SystemExit
#    # here :-(, and try again.
#    if 'install' not in sys.argv or 'ext_modules' not in setup_args:
#        # We weren't trying to install an extension, so forget it.
#        raise
#    msg = "Couldn't install with extension module, trying without it..."
#    exc = sys.exc_info()[1]
#    exc_msg = "%s: %s" % (exc.__class__.__name__, exc)
#    print("**\n** %s\n** %s\n**" % (msg, exc_msg))
#
#    del setup_args['ext_modules']
#    setup(**setup_args)