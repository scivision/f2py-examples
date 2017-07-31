#!/usr/bin/env python

req = ['nose','numpy']

try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    import pip
    pip.main(['install'] + req)

# %%
import setuptools #needed to enable develop
from numpy.distutils.core import setup,Extension

ext=[Extension(name='pyprod',
               sources=['fortprod.f90'],
               f2py_options=['--quiet'],
    )]

#%% install
setup(name='demof2py',
	 description='demo Python wrap of Fortran',
	 author='Michael Hirsch, Ph.D.',
	 url='https://github.com/scivision/f2pyExamples',
     version='0.1',
     ext_modules=ext,
     install_requires=req,
      )


