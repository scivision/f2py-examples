cmake_minimum_required(VERSION 3.7)
project(tetran Fortran)
enable_testing()


add_library(prod prod.f90)

add_executable(prod_test tests/prog_fortprod.f90)
target_link_libraries(prod_test prod)
