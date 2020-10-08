#ifndef GRAPHMATRIX_MATRIX_H
#define GRAPHMATRIX_MATRIX_H

#endif //GRAPHMATRIX_MATRIX_H

#include "stdlib.h"
#include "operations/remvrtx.h"

void define_matrx_poiners(int** m, int size);

int** matrix_create(int size);

void matrix_free(int** matrix,int size);

void init_random_symetric_matrix(int** matrix, int size, float chance);

void init_empty_matrix(int** matrix, int size);
