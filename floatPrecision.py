#!/usr/bin/env python
"""
Demonstrates limits of IEEE754 floating point precision, relevant to Fortran 
which is often single-precision (32-bit)

see Wikipedia "unit in the last place" "machine epsilon"
"Machine epsilon is defined as the smallest number that, when added to one, yields a result different from one."

Reference: Matlab/Octave
>> eps(double(1))
ans =    2.2204e-16

>> eps(single(1))
ans =    1.1921e-07
"""
from numpy import float32

px=0
x=float32(1)

while x != x + float32(1):
    x *= float32(2)
    px += 1

eps32= 2**(-(px-1))
print('bits of precision for 32-bit float',px)
print('machine epsilon: 32-bit float',eps32)
#%%
py=0
y=1.

while y != y + 1:
    y *= 2.
    py += 1
    
eps64= 2**(-(py-1))
print('bits of precision for 64-bit float',py)
print('machine epsilon: 64-bit float',eps64)