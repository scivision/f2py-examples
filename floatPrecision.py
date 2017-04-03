#!/usr/bin/env python
"""
Demonstrates limits of IEEE754 floating point precision, relevant to Fortran 
which is often single-precision (32-bit)

see Wikipedia "unit in the last place"

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

print('bits of precision for 32-bit float',px)
print('Unit in the last place: finest step 32-bit float',1/2**px)
print('finest step -1 + finest step +1',1/2**px-1 + 1/2**px+1)
#%%
py=0
y=1.

while y != y + 1:
    y *= 2.
    py += 1
    
print('bits of precision for 64-bit float',py)
print('Unit in the last place: finest step 32-bit float',1/2**py)
print('finest step -1 + finest step +1',1/2**py-1 + 1/2**py+1)