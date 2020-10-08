#include "matrix.h"

static int one_or_zero(float chance){
    int a = rand()%100;

    int result;

    if ((float)a<(100*chance)){
        result = 1;
    }
    else{
        result = 0;
    }

    return result;
}

void init_empty_matrix(int** matrix, int size){
    for (int i=0; i<size; i++){
        for (int j=0; j<size;j++ ){
            matrix[i][j]=0;
        }
    }
}

void init_random_symetric_matrix(int** matrix, int size, float chance){
    int c=0;

    int i,j;
    for (i=c; i<size; i++){
        for (j=c; j<size;j++ ) {
            matrix[i][j] = one_or_zero(chance);
            matrix[j][i] = matrix[i][j];
        }
        c++;
    }

    //обнуление диагонали
    for (i=0; i<size; i++){
        matrix[i][i] = 0;
    }


}

void define_matrx_poiners(int** m, int size){
    m[0] = (int*)(m + size);
    for (int i = 1; i < size; i++) {
        m[i] = m[0] + i * size;
    }
}

int** matrix_create(int size){
    int** matrix = (int**)malloc(size*sizeof(int*));

    for(int i=0; i<size; i++){
        matrix[i] = (int*)malloc(size*sizeof(int));
    }

    return matrix;
}

void matrix_free(int** matrix,int size){
    for(int i=0; i<size; i++){
        free(matrix[i]);
    }

    free(matrix);
}