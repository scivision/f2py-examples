! this program should return "6." for each print

Program prodfort
use prod
implicit none
real x,y
real znoint,zint,zinout,zpure

x=3.
y=2.

call prodnointent(x,y,znoint)
print *, znoint

call prodintent(x,y,zint)
print *, zint

zinout=-1.
call prodinout(x,y,zinout)
print *,zinout

zpure = prodpure(x,y)
print *,zpure

End Program
