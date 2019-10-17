#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension


setup(ext_modules=[
    Extension(name='pyprod', sources=['prod.f90']),
    Extension(name='badprec', sources=['badprec.f90'])])
