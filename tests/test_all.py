#!/usr/bin/env python
import numpy as np
from pyprod import prod
import pytest

def test_main():
    x=3
    y=2
    #%%
    zint = prod.prodintent(x,y)
    assert zint == x*y
    assert isinstance(zint,float) #the Fortran code casts to float
    #%%
    znoint = 12345.
    znointent = prod.prodnointent(x,y,znoint)
    assert znointent is None
    assert np.isclose(znoint,12345.) #unmodified due to f2py intent(in) by default
    #%%
    zpure = prod.prodpure(x,y)
    assert zpure == x*y
    #%%
    zinout = np.array(23456.) #MUST be an ndarray e.g. 0d ndarray for scalar case!
    prod.prodinout(x,y,zinout)
    assert zinout==x*y

if __name__ =='__main__':
    pytest.main()
