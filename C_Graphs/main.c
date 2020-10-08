#include "time.h"
#include "matrix/mtrxgrph.h"

int main() {
    int size1 = 5;
    int begin1 = 1;

    float chance1=0.5;
    float chance2=0.3;

    mtrx_grph_t* G1 = matrixGraph_create(size1,begin1);

    srand(time(NULL));
    init_random_symetric_matrix(G1->matrix,size1,chance1);

    print_graph(G1);

//    remove_vrtx_sectors(G1,1);

    add_vrtx(G1);

    print_graph(G1);

//    matrixGraph_free(G1);

    return 0;
}
