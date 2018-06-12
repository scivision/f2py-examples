#!/usr/bin/env python
install_requires = ['numpy']
tests_require = ['pytest', 'coveralls']
# %%
from setuptools import find_packages
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
     install_requires=install_requires,
     tests_require=tests_require,
     extras_require={'tests': tests_require},
     python_requires='>=2.7',
      )


