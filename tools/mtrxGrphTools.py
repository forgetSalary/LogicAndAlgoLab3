import random

def printMatrixGraph(graph):
    rng=range(len(graph.matrix))

    print('|v{:>2s}|{:<3s}|'.format("",""), end='')
    for i in graph.vertexes:
        print("{:<3d}|".format(i), end='')
    print('', end="\n|{:<3s}|".format(""))

    for i in rng:
        print("{:<3s}|".format(""), end='')
    print('{:<3s}|'.format(""), end='\n')

    for i in rng:
        print("|{:>3d}|{:<3s}".format(graph.vertexes[i],""), end='')
        for j in rng:
            print("|{:<3d}".format(graph.matrix[i][j]),end='')
        print('|',end='\n')
    print('', end='\n')

# def printGraph(graph):
#     rng=range(len(graph.matrix))
#
#     print(graph.vertexes)
#
#     for i in rng:
#         for j in rng:
#             print("%d,"%(graph.matrix[i][j]),end='')
#         print('',end='\n')
#     print('', end='\n')

def randomVertice(chance):
    a=random.choice(list(range(100)))

    if a<int(100*chance):
        res=1
    else:
        res=0

    return res

def makeVertexes(size):
    rng=list(range(1,size*2+1))

    names=[]
    for i in range(size):
        name=random.choice(rng)
        del rng[rng.index(name)]
        names.append(name)

    names.sort()

    return names

def randomMatrixGraph(size,density):
    rng=list(range(size))

    matrix = [[0 for i in range(size)] for i in range(size)]

    for i in rng:
        for j in rng:
            matrix[i][j] = randomVertice(density)
            matrix[j][i] = matrix[i][j]
        matrix[i][i] = 0 #убираем петлю
        del rng[0]
    return matrix

def xor(a,b):
    if a == b:
        return 0
    else:
        return 1

def arrOr(vrtxs1, vrtxs2):
    newVrtxs = [i for i in vrtxs1]

    for i in range(len(vrtxs2)):
        if (vrtxs2[i] not in newVrtxs):
            newVrtxs.append(vrtxs2[i])

    return newVrtxs

def arrAnd(vrtxs1, vrtxs2):
    newVrtxs = []

    for i in range(len(vrtxs2)):
        if (vrtxs2[i] in vrtxs1):
            newVrtxs.append(vrtxs2[i])

    return newVrtxs

def arrXor(vrtxs1, vrtxs2):
    newVrtxs = []

    for i in range(len(vrtxs2)):
        if (vrtxs2[i] not in newVrtxs):
            newVrtxs.append(vrtxs2[i])

    return newVrtxs