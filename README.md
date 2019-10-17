[![Actions Status](https://github.com/scivision/f2py-examples/workflows/ci/badge.svg)](https://github.com/scivision/f2py-examples/actions)

# f2py Examples


Simple examples of using `f2py` to get high-speed Fortran integrated with Python easily.
These examples are also useful to troubleshoot problems with `f2py`.

## Build

Fortran compiler is needed:

* Mac: `brew install gcc`
* Linux: `apt install gfortran`  or  `yum install gfortran`
* [Windows](https://www.scivision.dev/install-latest-gfortran-on-ubuntu/)

### Install

```sh
pip install -e .
```

This will compile the Fortran code (in `.f` and `.f90` files).
It creates a file `pyprod.*` where `*` depends on operating system and Python version:

* Linux/Mac: `.so`
* Windows: `.pyd`

## Examples

### .f2py_cmap required

A file `.f2py_cmap` as in this repository must be in the top-level (same as setup.py) of the project directory tree.
If this file is missing, all "real" kinds map to float32, which is not in general what is wanted.
A missing .f2py_cmap will lead float64 values to be completely incorrect.

The names in the .f2py_cmap must exactly match the Fortran variable names used for the real kind.
If you use dp=>real64 in the Fortran code, then .f2py_cmap must map `dp` as well.

### Fortran Intents

```sh
python f2py_demo.py
```
You will see the output:
```
x = 3
y = 2
x * y = 6.0
Your system did this in Python using Fortran-compiled library
```

### Fortran comment syntax

Fortran 77 is officially full-line comments only. Inline comments are
not allowed with `f2py` as a result in Fortran 77 files. Demonstrate
this with:
```sh
f2py -m badcomment -c badcomment.f
```

## Troubleshooting f2py

`f2py` normally Just Works on Linux, Mac and
[Windows Subsystem for Linux](https://www.scivision.dev/tags/windows-subsystem-for-linux).
However, Windows itself can be more challenging due to inconsistencies in Microsoft Visual Studio.

See the Windows f2py installation guide and troubleshooting
[guide](https://www.scivision.dev/f2py-running-fortran-code-in-python-on-windows/).
