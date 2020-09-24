import random

def xor(a,b):
    if a == b:
        return 0
    else:
        return 1

def randomMatrixGraph(n):
    rng=list(range(n))

    matrix = [[0 for i in range(n)] for i in range(n)]

    for i in rng:
        for j in rng:
            matrix[i][j] = random.choice([0, 1])
            matrix[j][i] = matrix[i][j]
        del rng[0]
    return matrix

def printGraph(graph):
    rng=range(len(graph))

    print('|v| |', end='')
    for i in rng:
        print("%d|" %i, end='')
    print('', end="\n| |")

    for i in rng:
        print(" |", end='')
    print(' |', end='\n')

    for i in rng:
        print("|%d| "% (i), end='')
        for j in rng:
            print("|%d"%(graph[i][j]),end='')
        print('|',end='\n')
    print('', end='\n')

def printGraph2(graph):
    rng=range(len(graph))

    for i in rng:
        for j in rng:
            print("%d,"%(graph[i][j]),end='')
        print('',end='\n')
    print('', end='\n')

def otozhdestvVer(graph,v,u):
    gsize=len(graph)

    rng = list(range(gsize))

    #делаем объединения ребер вершин u и v
    for i in range(gsize):
        if i!=v:
            graph[v][i]=graph[v][i] or graph[u][i]
            graph[i][v] = graph[v][i]

    #удаляем ненужные ребра
    for i in range(gsize):
        del graph[i][u]

    #удаляем вершину u
    del graph[u]

def styanRebro(graph,v,u):
    #проверяем на смежность
    if (graph[v][u]==1):
        otozhdestvVer(graph, v, u)
        return True
    else:
        return False

def rasshepVer(graph,v):
    gsize=len(graph)

    new_vertx=[graph[v][i] for i in range(gsize)]

    new_vertx.append(graph[v][v])

    graph.append(new_vertx)

    for i in range(gsize):
        graph[i].append(graph[v][i])

def obedin(graph1,graph2):
    gsize1 = len(graph1)
    gsize2 = len(graph2)

    gsize= min(gsize1,gsize2)

    if gsize==gsize1:
        oldgraph = graph1
        newgraph = graph2
    else:
        oldgraph = graph2
        newgraph = graph1

    rng=list(range(gsize))
    for i in rng:
        for j in rng:
            newgraph[i][j] = newgraph[i][j] or oldgraph[i][j]
            newgraph[j][i] = newgraph[i][j]
        del rng[0]

    return newgraph

def peresechenie(graph1,graph2):
    gsize1 = len(graph1)
    gsize2 = len(graph2)

    gsize= min(gsize1,gsize2)

    if gsize==gsize1:
        oldgraph = graph1
        newgraph = graph2
    else:
        oldgraph = graph2
        newgraph = graph1

    rng=list(range(gsize))
    for i in rng:
        for j in rng:
            newgraph[i][j] = newgraph[i][j] and oldgraph[i][j]
            newgraph[j][i] = newgraph[i][j]
        del rng[0]

    return newgraph

def xorGraphs(graph1,graph2):
    gsize1 = len(graph1)
    gsize2 = len(graph2)

    gsize= min(gsize1,gsize2)

    if gsize==gsize1:
        oldgraph = graph1
        newgraph = graph2
    else:
        oldgraph = graph2
        newgraph = graph1

    rng=list(range(gsize))
    for i in rng:
        for j in rng:
            newgraph[i][j] = xor(newgraph[i][j],oldgraph[i][j])
            newgraph[j][i] = newgraph[i][j]
        del rng[0]

    return newgraph