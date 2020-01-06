module badprec

!! shows how f2py just assumes all real are float32
!! unless kind matches file .f2py_f2cmap

use, intrinsic :: iso_fortran_env, only: real32, real64

implicit none

real(real64), parameter :: pi64 = 4*atan(1.)
!! This will not be 3.1415... unless real64 is in .f2py_cmap

real(real32), parameter :: pi32 = 4*atan(1.)

end module badprec
