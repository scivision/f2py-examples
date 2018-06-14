#!/usr/bin/env python
from numpy.distutils.core import setup, Extension

install_requires = ['numpy']
tests_require = ['pytest', 'coveralls', 'flake8', 'mypy']

ext = [Extension(name='pyprod',
                 sources=['fortprod.f90'],
                 f2py_options=['--quiet'],
                 )]

# %% install
setup(name='demof2py',
      description='demo Python wrap of Fortran',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/f2pyExamples',
      version='0.5.0',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      ext_modules=ext,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      python_requires='>=2.7',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7', ]
      )
