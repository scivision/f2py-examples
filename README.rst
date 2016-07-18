=============
demo f2py
=============

Here's a simple example of using f2py to run Fortran code from Python

.. contents::

Minimal working example
=======================
::

    make

    python f2py_demo.py

Elemental and Real: Fortran Functions
=====================================
At this time (Numpy 1.10) f2py understands Pure Fortran functions, but does not understand Elemental Fortran functions (which are implicitly Pure).

Note on Intent(inout)
=====================
If the subroutine you want to interface Python with has the Fortran statement for a particular variable::

    Intent(inout) :: myvariable
    
This ``Intent(inout)`` means the variable is modified **in place**, it is *not* on the left hand side of the equals sign in Python.
