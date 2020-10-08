from tools.mtrxGrphTools import *

class mtrxGraph(object):
    def __init__(self,matrix,vertexes):
        self.matrix = matrix
        self.vertexes = vertexes

def removeVertx(graph,index):
    gsize = len(graph.matrix)

    # удаляем столбец
    for i in range(gsize):
        del graph.matrix[i][index]

    # удаляем строку
    del graph.matrix[index]

    #удаляем нвзвание вершины
    del graph.vertexes[index]

def addVertx(graph,vrtx):
    gsize = len(graph.matrix)

    #добавляем столбец
    for i in range(gsize):
        graph.matrix[i].append(0)

    #добавляем строку
    graph.matrix.append([0 for i in range(gsize)])

    graph.vertexes.append(vrtx)

def copyVerteces(dst, src, vrtx):
    srcIndex1 = src.vertexes.index(vrtx)
    dstIndex1 = dst.vertexes.index(vrtx)

    zeroes=0;
    #копируем ребра
    for i in src.vertexes:
        if i in dst.vertexes:
            dstIndex2 = dst.vertexes.index(i)
            srcIndex2 = src.vertexes.index(i)

            dst.matrix[dstIndex1][dstIndex2] = src.matrix[srcIndex1][srcIndex2]
            dst.matrix[dstIndex2][dstIndex1] = dst.matrix[dstIndex1][dstIndex2]

            if (not dst.matrix[dstIndex2][dstIndex1]):
                zeroes +=1

    if zeroes==len(src.vertexes):
        return 0
    else:
        return 1

def otozhdestvVer(graph,vrtx1,vrtx2):
    v = graph.vertexes.index(vrtx1)
    u = graph.vertexes.index(vrtx2)

    gsize = len(graph.matrix)

    rng = list(range(gsize))

    #делаем объединения ребер вершин u и v
    for i in range(gsize):
        if i!=v:
            graph.matrix[v][i] = graph.matrix[v][i] or graph.matrix[u][i]
            graph.matrix[i][v] = graph.matrix[v][i]

    removeVertx(graph, u)

def styanRebro(graph,v,u):
    #проверяем на смежность
    if (graph.matrix[v][u]==1):
        otozhdestvVer(graph, v, u)
        return True
    else:
        return False

def rasshepVer(graph,vrtx,divide):
    gsize = len(graph.matrix)
    v = graph.vertexes.index(vrtx)

    graph.vertexes.append(graph.vertexes[-1] + 1)

    if (divide):
        q = graph.matrix[v].count(1)//2

        new_vertx = [0 for i in range(gsize)]
        graph.matrix.append(new_vertx)

        for i in range(gsize):
            graph.matrix[i].append(0)
            if (graph.matrix[v][i] and q !=0):
                graph.matrix[-1][i] = graph.matrix[v][i]
                graph.matrix[i][-1] = (graph.matrix[v][i])
                graph.matrix[v][i] = 0
                q -= 1

            if (q == 0):
                graph.matrix[-1][i] = 0
                graph.matrix[i][-1] = 0

    else:
        new_vertx = [graph.matrix[v][i] for i in range(gsize)]

        new_vertx.append(0)

        graph.matrix.append(new_vertx)

        for i in range(gsize):
            graph.matrix[i].append(graph.matrix[v][i])

def obedin(graph1,graph2):
    newVertexex = arrOr(graph1.vertexes,graph2.vertexes)
    newSize = len(newVertexex)

    newRng=list(range(newSize))

    newMatrix= [[0 for i in newRng] for i in newRng]

    newGraph = mtrxGraph(newMatrix,newVertexex)

    for i in newRng:
        newVrtx1=newGraph.vertexes[i]

        if (newVrtx1 in graph1.vertexes):
            v1_1 = graph1.vertexes.index(newVrtx1)
            if (newVrtx1 in graph2.vertexes):
                v2_1 = graph2.vertexes.index(newVrtx1)

                for j in newRng:
                    newVrtx2 = newGraph.vertexes[j]

                    if (newVrtx2 in graph1.vertexes and newVrtx2 in graph2.vertexes):
                        v1_2 = graph1.vertexes.index(newVrtx2)
                        v2_2 = graph2.vertexes.index(newVrtx2)

                        nv1 = newGraph.vertexes.index(newVrtx1)
                        nv2 = newGraph.vertexes.index(newVrtx2)

                        newGraph.matrix[nv1][nv2] = graph1.matrix[v1_1][v1_2] or graph2.matrix[v2_1][v2_2]
                        newGraph.matrix[nv2][nv1] = newGraph.matrix[i][j]

            else:
                copyVerteces(newGraph, graph1, newVrtx1)
        else:
            copyVerteces(newGraph, graph2, newVrtx1)


    return newGraph

def peresechenie(graph1,graph2):
    newVertexex = arrAnd(graph1.vertexes, graph2.vertexes)
    newSize = len(newVertexex)

    if (newSize!=0):
        newRng = list(range(newSize))

        newMatrix = [[0 for i in newRng] for i in newRng]

        newGraph = mtrxGraph(newMatrix, newVertexex)

        for i in range(newSize):
            newVrtx1 = newGraph.vertexes[i]

            v1_1 = graph1.vertexes.index(newVrtx1)
            v2_1 = graph2.vertexes.index(newVrtx1)
            for j in newRng:
                newVrtx2 = newGraph.vertexes[j]

                v1_2 = graph1.vertexes.index(newVrtx2)
                v2_2 = graph2.vertexes.index(newVrtx2)

                newGraph.matrix[i][j] = graph1.matrix[v1_1][v1_2] and graph2.matrix[v2_1][v2_2]
                newGraph.matrix[j][i] = newGraph.matrix[i][j]

            del newRng[0]

        return newGraph

    else:
        return None

def koltsevaya_summa(graph1,graph2):
    newVertexex = arrOr(graph1.vertexes, graph2.vertexes)
    newSize = len(newVertexex)

    if (newSize != 0):
        newRng = list(range(newSize))

        newMatrix = [[0 for i in newRng] for i in newRng]

        newGraph = mtrxGraph(newMatrix, newVertexex)

        zeros=0
        forRemove=[]

        for i in range(newSize):
            newVrtx1 = newGraph.vertexes[i]

            if (newVrtx1 in graph1.vertexes):
                v1_1 = graph1.vertexes.index(newVrtx1)
                if (newVrtx1 in graph2.vertexes):
                    v2_1 = graph2.vertexes.index(newVrtx1)
                    for j in newRng:
                        newVrtx2 = newGraph.vertexes[j]

                        if (newVrtx2 in graph1.vertexes and newVrtx2 in graph2.vertexes):
                            v1_2 = graph1.vertexes.index(newVrtx2)
                            v2_2 = graph2.vertexes.index(newVrtx2)

                            newGraph.matrix[i][j] = xor(graph1.matrix[v1_1][v1_2],graph2.matrix[v2_1][v2_2])
                            newGraph.matrix[j][i] = newGraph.matrix[i][j]

                            if (not newGraph.matrix[i][j]):
                                zeros += 1

                    if zeros == newSize:
                        forRemove.append(i)

                    zeros=0
                else:
                    if (not copyVerteces(newGraph, graph1, newVrtx1)):
                        forRemove.append(i)
            else:
                if (not copyVerteces(newGraph, graph2, newVrtx1)):
                    forRemove.append(i)

        #удаление изолированных вершины
        for i in forRemove:
            removeVertx(newGraph,i)

        return newGraph

    else:
        return None

def smezhnost(graph,V,U):
    i = graph.vertexes.index(U)
    j = graph.vertexes.index(V)

    return graph.matrix[i][j]

def decart_graph_prod(graph1,graph2):
    new_vertexes=cart_prod(graph1.vertexes, graph2.vertexes)

    size1 = len(graph1.vertexes)
    size2 = len(graph2.vertexes)

    new_size = len(new_vertexes)
    new_range = range(new_size)

    new_matrix = [[0 for i in new_range] for i in new_range]

    new_graph = mtrxGraph(new_matrix,new_vertexes)

    condition = False
    for i in new_range:
        new_vrtx1=new_graph.vertexes[i]

        u = new_vrtx1[:new_vrtx1.index('&')]
        U = new_vrtx1[new_vrtx1.index('&')+1:]

        for j in new_range:
            new_vrtx2=new_graph.vertexes[j]

            v = new_vrtx2[:new_vrtx2.index('&')]
            V = new_vrtx2[new_vrtx2.index('&') + 1]

            if u==v:
                if smezhnost(graph2,U,V):
                    condition=True
                else:
                    condition = False

            elif U==V:
                if smezhnost(graph1,u,v):
                    condition = True
                else:
                    condition = False

            if condition:
                new_graph.matrix[i][j] = 1
                condition = False

    return new_graph