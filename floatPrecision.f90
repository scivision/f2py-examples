
use,intrinsic:: iso_fortran_env, only: sp=>real32, dp=>real64, qp=>real128
implicit none


integer :: ps,pd,pq
real(sp) :: eps32,  s
real(dp) :: eps64,  d
real(qp) :: eps128, q

! ----- single prec -------
ps=0
s=1.

do while (s /= s + 1.)
  s = s * 2.
  ps = ps + 1
end do

eps32 = 2.**(-(ps-1.))
print *, 'bits of precision for 32-bit float', ps
print *, 'machine epsilon: 32-bit float', eps32
! ----- double prec -------
pd=0
d=1._dp

do while (d /= d + 1._dp)
  d = d * 2._dp
  pd = pd + 1
end do

eps64 = 2._dp**(-(pd-1._dp))
print *, 'bits of precision for 64-bit float', pd
print *, 'machine epsilon: 64-bit float', eps64
! ----- quad prec -------
pq=0
q=1._qp

do while (q /= q + 1._qp)
  q = q * 2._qp
  pq = pq + 1
end do

eps128 = 2._qp**(-(pq-1._qp))
print *, 'bits of precision for 128-bit float', pq
print *, 'machine epsilon: 128-bit float', eps128

end program
