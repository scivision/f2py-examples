SRC=fortprod.f90
MAIN=prog_fortprod.f90
#----------------
FFLAGS = -std=f2008 -Wall -pedantic -Wextra -mtune=native -fexternal-blas -O3


OBJS=$(SRC:.f90=.o)
MOBJS=$(OBJS) $(MAIN:.f90=.o)

%.o: %.f90
	$(FC) $(FFLAGS) -c $<

all: prod.out

prod.out: $(MOBJS)
	$(FC) -o $@ $(MOBJS) $(FFLAGS)

clean:
	$(RM) $(MOBJS)

