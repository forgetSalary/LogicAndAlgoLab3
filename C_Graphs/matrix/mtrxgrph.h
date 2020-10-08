#ifndef GRAPHMATRIX_MTRXGRPH_H
#define GRAPHMATRIX_MTRXGRPH_H

#endif //GRAPHMATRIX_MTRXGRPH_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "matrix.h"

typedef struct matrix_graph{
    int** src;

    int** matrix;
    int* vertexes;
    int size;

}mtrx_grph_t;

mtrx_grph_t* matrixGraph_create(int size, int begin);

void remove_vrtx_memmove(mtrx_grph_t* graph, int vrtxindex);

void remove_vrtx_sectors(mtrx_grph_t* graph, int vrtxindex);

void add_vrtx(mtrx_grph_t* graph);

void print_graph(mtrx_grph_t* graph);

void matrixGraph_free(mtrx_grph_t* graph);

int int_index(int* array, int size, int value);
