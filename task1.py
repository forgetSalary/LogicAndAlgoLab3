from graph import randomMatrixGraph,printGraph,printGraph2

def task1():
    size = int(input("Введите количество вершин графа:"))

    graph1 = randomMatrixGraph(size)
    graph2 = randomMatrixGraph(size)

    print("G1:")
    printGraph2(graph1)

    print("G2:")
    printGraph(graph2)
