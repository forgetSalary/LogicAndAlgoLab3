cmake_minimum_required(VERSION 3.17)
project(GraphMatrix C)

set(CMAKE_C_STANDARD 99)

add_executable(GraphMatrix main.c matrix/matrix.h matrix/matrix.c matrix/mtrxgrph.h matrix/mtrxgrph.c lists/lists.h lists/listsGraph.h lists/listsGraph.c lists/lists.c matrix/operations/remvrtx.c matrix/operations/remvrtx.h)