#include "mtrxgrph.h"

int int_index(int* array, int size, int value){
    int indx=0;

    for (int i=0; i<size;i++) {
        if (array[i]==value){
            return indx;
        }
        else{
            indx++;
        }
    }

    return -1;
}

static int* vertexes_create(int size, int begin){
    int* vertexes = malloc(size*sizeof(int));

    for (int i=0; i<size;i++){
        vertexes[i]=i+begin;
    }

    return vertexes;
}

void print_graph(mtrx_grph_t* graph){
    //header
    printf("|v%-2c|%3c|",' ',' ');

    for (int i=0; i<graph->size; i++){
        printf("%3d|",graph->vertexes[i]);
    }
    printf("\n|%3c|",' ');

    for (int i=0; i<graph->size; i++){

        printf("%3c|",' ');
    }
    printf("%3c|\n",' ');

    //matrix
    for (int i=0; i<graph->size; i++){
        printf("|%-3d|%3c",graph->vertexes[i],' ');
        for (int j=0; j<graph->size; j++){
            printf("|%3d",graph->matrix[i][j]);
        }
        printf("|\n");
    }
    printf("\n");
}

void matrixGraph_free(mtrx_grph_t* graph){
    free(graph->vertexes);
    matrix_free(graph->matrix,graph->size);
    free(graph);
}

mtrx_grph_t* matrixGraph_create(int size, int begin){
    mtrx_grph_t* graph = malloc(sizeof(mtrx_grph_t));

    graph->matrix = matrix_create(size);
    graph->src = graph->matrix;

    graph->vertexes = vertexes_create(size,begin);
    graph->size = size;

    return graph;
}

void remove_vrtx_memmove(mtrx_grph_t* graph, int vrtxindex){
    int data_size;

    int* dst;
    int* src;

    //удаляем строку
    data_size = (graph->size)*((graph->size)-vrtxindex);

    dst = &(graph->matrix[vrtxindex][0]);
    src = &(graph->matrix[vrtxindex+1][0]);

    intmove(dst,src,data_size);

    //удаляем столбец
    for (int i=0; i<graph->size;i++){
        dst = &(graph->matrix[i][vrtxindex]);
        src = &(graph->matrix[i][vrtxindex+1]);

        data_size=(graph->size)-vrtxindex;

        intmove(dst,src,data_size);
    }

    //удаляем название вершины
    dst = &(graph->vertexes[vrtxindex]);
    src = &(graph->vertexes[vrtxindex+1]);

    intmove(dst,src,graph->size-vrtxindex);

    graph->size--;
}

void remove_vrtx_sectors(mtrx_grph_t* graph, int vrtxindex){
    if (vrtxindex<(graph->size)/2){
        move_sector1(graph->matrix,graph->size,vrtxindex);
        move_sector2_less(graph->matrix,graph->size,vrtxindex);
        move_sector3_less(graph->matrix,graph->size,vrtxindex);

        move_matrix_pointers(graph->matrix,graph->size);
    }

    else{
        if (vrtxindex>(graph->size)/2){
            move_sector2_more(graph->matrix,graph->size,vrtxindex);
            move_sector3_more(graph->matrix,graph->size,vrtxindex);
            move_sector4(graph->matrix,graph->size,vrtxindex);

        }
        else{if(vrtxindex==0){
            move_matrix_pointers(graph->matrix,graph->size);
        }}

    }
    //удаляем название вершины
    int* dst = &(graph->vertexes[vrtxindex]);
    int* src = &(graph->vertexes[vrtxindex+1]);

    intmove(dst,src,graph->size-vrtxindex);

    graph->size--;
}

void add_vrtx(mtrx_grph_t* graph){
    int old_size=graph->size;

    graph->matrix = (int**)realloc(graph->matrix, (old_size+1) * sizeof(int*));
    graph->matrix[old_size] =(int*)malloc((old_size+1)* sizeof(int));

    for (int i = 0; i < old_size; i++){
        graph->matrix[i] = (int*)realloc(graph->matrix[i], (old_size+1)* sizeof(int));
    }

    graph->size++;
    int new_size=graph->size;

    graph->src = graph->matrix;
    graph->vertexes = realloc(graph->vertexes,sizeof(int)*new_size);

    for (int i=0; i<new_size; i++){
        graph->matrix[new_size-1][i]=0;
        graph->matrix[i][new_size-1]=0;

    }

    graph->vertexes[new_size-1]=graph->vertexes[new_size-2]+1;
}