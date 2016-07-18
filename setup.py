#!/usr/bin/env python
import setuptools #needed to enable develop
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass

from numpy.distutils.core import setup,Extension

ext=[Extension(name='pyprod',
               sources=['fortprod.f90'],
               f2py_options=['--quiet'],
    )]

#%% install
setup(name='demof2py',
	 description='demo Python wrap of Fortrna',
	 author='Michael Hirsch',
	 url='https://github.com/scienceopen/f2pyExamples',
     ext_modules=ext,
      )


