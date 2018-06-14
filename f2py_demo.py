#!/usr/bin/env python
"""
demo of need to use INTENT() in the Fortran code with f2py
as current versions of f2py assume INTENT(IN), which is an obvious
issue for getting results back to Python!

Note: imports from f2py will always be ALL lowercase!
"""
import numpy as np
from pyprod import prod


x = 3
y = 2
# %%
zint = prod.prodintent(x, y)
assert zint == x*y
assert isinstance(zint, float)  # the Fortran code casts to float
# %%
znoint = 12345.
znointent = prod.prodnointent(x, y, znoint)
assert znointent is None
# unmodified due to f2py intent(in) by default
assert np.isclose(znoint, 12345.)
# %%
zpure = prod.prodpure(x, y)
assert zpure == x*y
# %%
# MUST be an ndarray e.g. 0d ndarray for scalar case!
zinout = np.array(23456.)
prod.prodinout(x, y, zinout)
assert zinout == x*y

print('x =', x)
print('y =', y)
print('x * y =', zint)
print('Your system did this in Python using Fortran-compiled library')
