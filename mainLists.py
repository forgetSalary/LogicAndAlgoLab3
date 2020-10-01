from graphs.listGraph import *
from graphs.matrixGraph import *

def main():
    m1 = [[0, 1, 1, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 1],
          [0, 0, 1, 0]]

    v1 = [1, 2, 6, 9]

    mtrrxG1=mtrxGraph(m1,v1)
    G1=matrixToList(mtrrxG1)
    printListGraph(G1)

    otozhdestvVer_List(G1,1,6)
    printListGraph(G1)



if __name__ == '__main__':
    main()
