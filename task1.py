import os
from graph import randomMatrixGraph,printGraph

def task1():
    size1 = int(input("Введите количество вершин графа 1:"))

    graph1 = randomMatrixGraph(size1)

    print("G1:")
    printGraph(graph1)

    size2 = int(input("Введите количество вершин графа 1:"))

    graph2 = randomMatrixGraph(size2)

    print("G2:")
    printGraph(graph2)
