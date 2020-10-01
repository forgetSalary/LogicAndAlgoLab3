from tasks.task2 import *
from tasks.task3 import *

def main():
    cntn = 1

    H = None

    # task1
    # size1 = int(input("Введите количество вершин графа 1: "))
    # dns1 = float(input("Плотность графа 1: "))
    # G1 = mtrxGraph(randomMatrixGraph(size1, dns1), makeVertexes(size1))
    #
    # size2 = int(input("\nВведите количество вершин графа 2: "))
    # dns2 = float(input("Плотность графа 2: "))
    # G2 = mtrxGraph(randomMatrixGraph(size2, dns2), makeVertexes(size2))

    m1=[[0,1,1,0],
        [1,0,0,0],
        [1,0,0,1],
        [0,0,1,0]]

    v1 = [1, 2, 6, 9]

    G1 = mtrxGraph(m1,v1)

    m2=[[0,1,0,0],
        [1,0,1,0],
        [0,1,0,0],
        [0,0,0,0]]


    v2 = [1, 2, 9, 10]

    G2 = mtrxGraph(m2, v2)


    msvcrt.getch()
    while(cntn):
        os.system('cls')

        print("G1:")
        printMatrixGraph(G1)

        print("G2:")
        printMatrixGraph(G2)

        print("Выберети задание (2 или 3):\n")
        task= int(msvcrt.getch())

        if (task == 2):
            os.system('cls')

            print("G1:")
            printMatrixGraph(G1)

            print("G2:")
            printMatrixGraph(G2)
            print("Выберети задание (1 или 2):\n")
            gr = int(msvcrt.getch())

            if (gr == 1):
                graph = G1
            else:
                graph = G1

            task2(graph)

        else:
            H = task3(G1,G2)

        print("\nПродолжить - 1, выйти - 0")
        cntn = int(msvcrt.getch())

if __name__ == '__main__':
    main()
