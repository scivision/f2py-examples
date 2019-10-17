#!/usr/bin/env python
"""
Demonstrates limits of IEEE754 floating point precision

see Wikipedia "unit in the last place" "machine epsilon"
"Machine epsilon is defined as the smallest number that, when added to one, yields a result different from one."

Compare with:

Matlab/Octave
-------------
>> eps(double(1)) =>    2.2204e-16

>> eps(single(1)) =>    1.1921e-07

https://blogs.mathworks.com/cleve/2017/05/22/quadruple-precision-128-bit-floating-point-arithmetic/

Matlab and Octave can support quad precision using external libraries, with great slowdowns in computing.
I would consider Fortran for a project needing quad precision

Fortran
-------
 bits of precision for 32-bit float          24
 machine epsilon: 32-bit float   1.19209290E-07
 bits of precision for 64-bit float          53
 machine epsilon: 64-bit float   2.2204460492503131E-016
 bits of precision for 128-bit float         113
 machine epsilon: 128-bit float   1.92592994438723585305597794258492732E-0034


Half precision:
---------------
GCC: currently only on ARM
https://gcc.gnu.org/onlinedocs/gcc/Half-Precision.html
Matlab: via external libraries.
Python: Numpy
"""
import numpy as np

# %% half prec
ph = 0
h = np.float16(1)

while h != h + np.float16(1):
    h *= np.float16(2)
    ph += 1

eps16 = 2 ** (-(ph - 1))
print('bits of precision for 16-bit float', ph)
print('machine epsilon: 16-bit float', eps16)

# %% single prec
ps = 0
s = np.float32(1)

while s != s + np.float32(1):
    s *= np.float32(2)
    ps += 1

eps32 = 2 ** (-(ps - 1))
print('bits of precision for 32-bit float', ps)
print('machine epsilon: 32-bit float', eps32)
# %% double prec
pd = 0
d = 1.0

while d != d + 1:
    d *= 2.0
    pd += 1

eps64 = 2 ** (-(pd - 1))
print('bits of precision for 64-bit float', pd)
print('machine epsilon: 64-bit float', eps64)
# %% quad prec
"""
caveats on Numpy "long double":
https://docs.scipy.org/doc/numpy-dev/user/basics.types.html#extended-precision
"""
pq = 0
q = np.float128(1.0)

while q != q + np.float128(1):
    q *= np.float128(2.0)
    pq += 1

eps128 = 2 ** (-(pq - 1))
print('bits of precision for long double', pq)
print('machine epsilon: long double', eps128)
