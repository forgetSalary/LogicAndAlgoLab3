import os
import msvcrt
from graphs.matrixGraph import *

def task3(G1,G2):
    os.system('cls')

    print("G1:")
    printMatrixGraph(G1)

    print("G2:")
    printMatrixGraph(G2)

    print("Выберети действие:\n"
          "1)Объединение\n"
          "2)Пересечение\n"
          "3)Кольцевая сумма")
    switch = int(msvcrt.getch())
    os.system('cls')

    print("G1:")
    printMatrixGraph(G1)

    print("G2:")
    printMatrixGraph(G2)


    newgraph = None

    if switch == 1:
        newgraph = obedin(G1, G2)
        print("H1:")
        printMatrixGraph(newgraph)

    elif switch == 2:
        newgraph = peresechenie(G1, G2)
        print("H1:")
        if newgraph!=None:
            printMatrixGraph(newgraph)
        else:
            print("Пустое множество")

    elif switch == 3:
        newgraph = xorGraphs(G1, G2)
        print("H1:")
        if newgraph != None:
            printMatrixGraph(newgraph)
        else:
            print("Пустое множество")

    return newgraph