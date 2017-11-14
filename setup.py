#!/usr/bin/env python
req = ['nose','numpy']
# %%
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
     python_requires='>=2.7',
      )


