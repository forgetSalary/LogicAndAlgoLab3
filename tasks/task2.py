import os
from graphs.matrixGraph import *

def task2(graph):
    print("Выберети действие:\n"
          "1)Отождествление вершин\n"
          "2)Стягивание ребра\n"
          "3)Расщепления вершины")
    switch = int(input())
    os.system('cls')

    if switch == 1:
        print("Отождествление вершин")
        ver1 = int(input("Введите вершину 1:"))
        ver2 = int(input("Введите вершину 2:"))

        otozhdestvVer(graph, ver1, ver2)

        print("Новый G1:")
        printMatrixGraph(graph)

    elif switch == 2:
        print("Стягивание ребра")
        ver1 = int(input("Введите вершину 1:"))
        ver2 = int(input("Введите вершину 2:"))

        if (styanRebro(graph, ver1, ver2)):
            print("Новый G1:")
            printMatrixGraph(graph)
        else:
            print("Вершины не смежные")

    elif switch == 3:
        print("Расщепления вершины")
        ver = int(input("Введите вершину:"))

        rasshepVer(graph, ver)

        print("Новый G1:")
        printMatrixGraph(graph)

