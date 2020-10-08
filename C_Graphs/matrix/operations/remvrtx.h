#ifndef GRAPHMATRIX_REMVRTX_H
#define GRAPHMATRIX_REMVRTX_H

#endif //GRAPHMATRIX_REMVRTX_H

void intmove(int* dst, int* src, int size);

void move_matrix_pointers(int** matrix, int size);

void move_sector1(int** matrix, int size, int vrtxindex);

void move_sector2_more(int** matrix, int size, int vrtxindex);

void move_sector3_more(int** matrix, int size, int vrtxindex);

void move_sector2_less(int** matrix, int size, int vrtxindex);

void move_sector3_less(int** matrix, int size, int vrtxindex);

void move_sector4(int** matrix, int size, int vrtxindex);