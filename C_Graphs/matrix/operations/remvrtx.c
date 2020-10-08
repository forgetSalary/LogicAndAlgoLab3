void intmove(int* dst, int* src, int size){
    for (int i=0;i<size;i++){
        *(dst+i)=*(src+i);
    }
}

void move_matrix_pointers(int** matrix, int size){
    for (int i = 0; i < size; i++) {
        matrix[i] += (size+1);
    }
}

void move_sector1(int** matrix, int size, int vrtxindex){
    for (int i=0; i<vrtxindex;i++){
        for (int j=0; j<vrtxindex;j++){
            matrix[i+1][j+1]=matrix[i][j];
        }
    }
}

void move_sector2_more(int** matrix, int size, int vrtxindex){
    int data_size;

    int* dst;
    int* src;

    for (int i=0; i<vrtxindex;i++){
        dst = &(matrix[i][vrtxindex]);
        src = &(matrix[i][vrtxindex+1]);

        data_size=size-vrtxindex-1;

        intmove(dst,src,data_size);
    }
}

void move_sector3_more(int** matrix, int size, int vrtxindex){
    for (int i=0; i<size-vrtxindex-1;i++){
        for (int j=0; j<vrtxindex;j++){
            matrix[vrtxindex+i][j]=matrix[vrtxindex+i+1][j];
        }
    }

}

void move_sector2_less(int** matrix, int size, int vrtxindex){
    for (int i=0; i<vrtxindex;i++){
        for (int j=0; j<size-vrtxindex-1;j++){
            matrix[vrtxindex-i][j]=matrix[vrtxindex-i-1][j];
        }
    }
}

void move_sector3_less(int** matrix, int size, int vrtxindex){
    int data_size;

    int* dst;
    int* src;

    for (int i=0; i<size-vrtxindex-1;i++){
        dst = &(matrix[i][vrtxindex-i]);
        src = &(matrix[i][vrtxindex-1-i]);

        data_size=vrtxindex;

        intmove(dst,src,data_size);
    }

}

void move_sector4(int** matrix, int size, int vrtxindex){
    for (int i=0; i<size-vrtxindex-1;i++){
        for (int j=0; j<size-vrtxindex-1;j++){
            matrix[vrtxindex+i][vrtxindex+j]=matrix[vrtxindex+i+1][vrtxindex+j+1];
        }
    }
}