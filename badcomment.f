! Example of disallowed non-full-line comment in Fortran 77 file by f2py.
! Most Fortran compilers allow this, but f2py is stricter to Fortran 77 standards.
! compare with permitted:
! f2py -m goodcomment90 -c goodcomment.f90
! f2py -m goodcomment77 -c goodcomment.f

      Subroutine BadComment

      real x

      common x ! bad for Fortran77

      end Subroutine BadComment
     
