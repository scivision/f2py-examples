#!/usr/bin/env python
from numpy.distutils.core import setup, Extension

setup(ext_modules=[Extension(name='pyprod',
                             sources=['prod.f90'],
                             f2py_options=['--quiet'],
                             )])
