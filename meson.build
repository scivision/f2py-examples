project('f2py-examples', 'fortran',
  default_options : ['default_library=static', 'buildtype=release'])

prod_lib = library('prod', 'prod.f90')

prod_test_exe = executable('prod_test', 'tests/prog_fortprod.f90',
  link_with: prod_lib)

floatprec_exe = executable('float_precision', 'floatPrecision.f90')
