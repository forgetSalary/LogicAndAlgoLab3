from graphs.listGraph import *
from graphs.matrixGraph import *

def main():
    # m1 = [[0, 1, 1, 0],
    #       [1, 0, 0, 0],
    #       [1, 0, 0, 1],
    #       [0, 0, 1, 0]]
    #
    # v1 = [1, 2, 6, 9]
    #
    # mtrxG1=mtrxGraph(m1,v1)

    mtrxG1 = mtrxGraph(randomMatrixGraph(13, 0.3), makeVertexes(13))
    mtrxG2 = mtrxGraph(randomMatrixGraph(5, 0.5), makeVertexes(5))

    G1=matrixToList(mtrxG1)
    G2 = matrixToList(mtrxG2)

    printListGraph(G1)
    printListGraph(G2)


if __name__ == '__main__':
    main()
