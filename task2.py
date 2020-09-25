import os
from graph import *

def task2():
    os.system('cls')
    size = int(input("Введите количество вершин графа:"))
    os.system('cls')

    print("Выберети действие:\n"
          "1)Отождествление вершин\n"
          "2)Стягивание ребра\n"
          "3)Расщепления вершины")
    switch=int(input())
    os.system('cls')

    graph = randomMatrixGraph(size)
    print("G1:")
    printGraph(graph)

    if switch==1:
        print("Отождествление вершин")
        ver1 = int(input("Введите вершину 1:"))
        ver2 = int(input("Введите вершину 2:"))

        otozhdestvVer(graph, ver1, ver2)

        print("H1:")
        printGraph(graph)

    elif switch==2:
        print("Стягивание ребра")
        ver1 = int(input("Введите вершину 1:"))
        ver2 = int(input("Введите вершину 2:"))

        if (styanRebro(graph, ver1, ver2)):
            print("H1:")
            printGraph(graph)
        else:
            print("Вершины не смежные")

    elif switch==3:
        print("Расщепления вершины")
        ver = int(input("Введите вершину:"))

        rasshepVer(graph,ver)

        print("H1:")
        printGraph(graph)

