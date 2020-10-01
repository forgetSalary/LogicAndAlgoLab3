from graphs.listGraph import *
from graphs.matrixGraph import *

def main():
    # m1 = [[0, 1, 1, 0],
    #       [1, 0, 0, 0],
    #       [1, 0, 0, 1],
    #       [0, 0, 1, 0]]
    #
    # v1 = [1, 2, 6, 9]

    mtrrxG1 = mtrxGraph(randomMatrixGraph(10, 0.6), makeVertexes(10))

    listG1 = listToMatrix(mtrrxG1)

    printMatrixGraph(mtrrxG1)
    printListGraph(listG1)

if __name__ == '__main__':
    main()
