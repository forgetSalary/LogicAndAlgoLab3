import os
from graph import *

def task3():
    os.system('cls')

    size1 = int(input("Введите количество вершин графа 1:"))
    os.system('cls')
    size2 = int(input("Введите количество вершин графа 2:"))
    os.system('cls')

    print("Выберети действие:\n"
          "1)Объединение\n"
          "2)Пересечение\n"
          "3)Кольцевая сумма")
    switch = int(input())
    os.system('cls')

    graph1 = randomMatrixGraph(size1)
    graph2 = randomMatrixGraph(size2)

    print("G1:")
    printGraph2(graph1)

    print("G2:")
    printGraph2(graph2)

    if switch == 1:
        newgraph=obedin(graph1,graph2)
        print("H1:")
        printGraph2(newgraph)

    elif switch == 2:
        newgraph = peresechenie(graph1, graph2)
        print("H1:")
        printGraph2(newgraph)

    elif switch == 3:
        newgraph = xorGraphs(graph1, graph2)
        print("H1:")
        printGraph2(newgraph)