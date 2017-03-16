#!/usr/bin/env python
import setuptools #needed to enable develop

#%% Monkey patch necessary since setup_requires is not adequate
import pip
pip.main(['install','numpy'])
#%% install
from numpy.distutils.core import setup,Extension

ext=[Extension(name='pyprod',
               sources=['fortprod.f90'],
               f2py_options=['--quiet'],
    )]

req = ['nose','numpy']

#%% install
setup(name='demof2py',
	 description='demo Python wrap of Fortran',
	 author='Michael Hirsch, Ph.D.',
	 url='https://github.com/scivision/f2pyExamples',
     version='0.1',
     ext_modules=ext,
     install_requires=req,
      )


