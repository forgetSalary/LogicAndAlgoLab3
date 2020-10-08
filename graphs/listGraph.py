from tools.listsGrphTools import *
from tools.mtrxGrphTools import arrOr, arrAnd


class Node(object):
    def __init__(self):
        self.vertex = None
        self.next = None

    def vrtxappend(self,vrtx):
        end=self

        while (end.next):
            end = end.next

        end.next = Node()

        end.next.vertex=vrtx

class listGraph(object):
    def __init__(self,lists,vertexes):
        self.lists=lists
        self.vertexes=vertexes

def matrixToList(matrixGraph):
    mtrxSize = len(matrixGraph.matrix)

    graphLists = [Node() for i in range(mtrxSize)]

    nextList,nextVertex = None, None

    for i in range(mtrxSize):
        nextList = graphLists[i]

        nextList.vertex = matrixGraph.vertexes[i]

        nextVertex = nextList

        for j in range(mtrxSize):
            if matrixGraph.matrix[i][j]:
                nextVertex.next = Node()
                nextVertex = nextVertex.next

                nextVertex.vertex=matrixGraph.vertexes[j]

    lgraph=listGraph(graphLists,matrixGraph.vertexes)

    return lgraph

def findInList(vlist,vrtxToFind):
    nextVertex = vlist

    found = None

    # если голова = vrtxToFind, вернуть ее
    if (nextVertex.vertex == vrtxToFind):
        return nextVertex

    while (nextVertex and nextVertex.vertex != vrtxToFind):
        nextVertex = nextVertex.next
        found = nextVertex


    return found

def findFirstParent(vlist,child):
    nextVertex = vlist

    parent = None

    # если вершина изолированная, вернуть ее
    if (nextVertex.vertex == child):
        return nextVertex

    while (nextVertex.vertex != child and nextVertex):
        parent =nextVertex
        nextVertex = nextVertex.next

    return parent


#directed
def removeVertx_List_drct(list, vrtx):
    nextVertex, vrtxForClear, parent = None, None, None

    nextVertex = list.next
    while (nextVertex):
        found = findFirstParent(list, vrtx)

        if found:
            found.next = found.next.next
            break
        else:
            nextVertex = nextVertex.next


# undirected
def removeVertx_List(graph, vrtx):
    v=graph.vertexes.index(vrtx)

    removeVertx_List_drct(graph.lists[v],vrtx)

    del graph.lists[v]
    del graph.vertexes[v]

def rasshepVer_List(graph,vrtx):
    v = graph.vertexes.index(vrtx)

    graph.lists.append(Node())
    graph.lists[-1].vertex = graph.lists[-2].vertex+1
    newVrtx=graph.lists[-1].vertex

    graph.vertexes.append(newVrtx)

    verteces=graph.lists[v].next
    graph.lists[-1].next=verteces

    nextVertex,vrtxforappend = None, None

    nextVertex=graph.lists[v].next
    while(nextVertex):
        vrtxforappend=graph.vertexes.index(nextVertex.vertex)

        graph.lists[vrtxforappend].vrtxappend(newVrtx)

        nextVertex=nextVertex.next

def otozhdestvVer_List(graph,vrtxDst,vrtxSrc):
    vrtx_index_Dst=graph.vertexes.index(vrtxDst)
    vrtx_index_Srs=graph.vertexes.index(vrtxSrc)

    dst_head = graph.lists[vrtx_index_Dst]
    src_head = graph.lists[vrtx_index_Srs]

    nextVertexOfSrc = src_head

    # удаляем ребро между Dst и Src, если оно есть
    vrtc_btw_dstsrc=findInList(dst_head, vrtxSrc)
    if (vrtc_btw_dstsrc):
        findFirstParent(dst_head, vrtxSrc).next = vrtc_btw_dstsrc.next

    # добавляем ребра из Src в Dst, если в последнем их нет
    while(nextVertexOfSrc.next):
        nextVertexOfSrc=nextVertexOfSrc.next

        found = findInList(dst_head,nextVertexOfSrc.vertex)
        if (not found):
            dst_head.vrtxappend(nextVertexOfSrc.vertex)

    del graph.vertexes[vrtx_index_Srs]
    del graph.lists[vrtx_index_Srs]

def styanRebro_List(graph,vrtxDst,vrtxSrc):
    vrtx_index_Dst = graph.vertexes.index(vrtxDst)
    vrtx_index_Srs = graph.vertexes.index(vrtxSrc)

    dst_head = graph.lists[vrtx_index_Dst]
    src_head = graph.lists[vrtx_index_Srs]

    # проверка на смежность
    if (findInList(dst_head, vrtxSrc) and (findInList(src_head, vrtxDst))):
        otozhdestvVer_List(graph, vrtxDst, vrtxSrc)
        return 1
    else:
        return 0

def obedin_List(graph1, graph2):
    newVertexes=arrOr(graph1.vertexes, graph2.vertexes)

    newSize =  len(newVertexes)

    newLists = [Node() for i in range(newSize)]
    for i in range(newSize):
        newLists[i].vertex = newVertexes[i]

    newGraph = listGraph(newLists,newVertexes)

    nextVrtx,found = None, None

    for i in range(newSize):
        newVrtx1 = newGraph.vertexes[i]

        if newVrtx1 in graph1.vertexes:
            v1 = graph1.vertexes.index(newVrtx1)

            newGraph.lists[i].next = graph1.lists[v1].next

            if newVrtx1 in graph2.vertexes:
                v2 = graph2.vertexes.index(newVrtx1)

                nextVrtx = graph2.lists[v2]

                while(nextVrtx):
                    found=findInList(newGraph.lists[i], nextVrtx.vertex)

                    if (not found):
                        newGraph.lists[i].vrtxappend(nextVrtx.vertex)

                    nextVrtx = nextVrtx.next

        else:
            v2 = graph2.vertexes.index(newVrtx1)
            newGraph.lists[i].next = graph2.lists[v2].next

    return newGraph

def peresechenie_List(graph1, graph2):
    newVertexes = arrAnd(graph1.vertexes, graph2.vertexes)

    newSize = len(newVertexes)

    newLists = [Node() for i in range(newSize)]
    for i in range(newSize):
        newLists[i].vertex = newVertexes[i]

    newGraph = listGraph(newLists, newVertexes)

    nextVrtx, found = None, None

    for i in range(newSize):
        newVrtx1 = newGraph.vertexes[i]

        v1 = graph1.vertexes.index(newVrtx1)
        v2 = graph2.vertexes.index(newVrtx1)

        nextVrtx = graph1.lists[v1].next

        while (nextVrtx):
            found = findInList(graph2.lists[v2], nextVrtx.vertex)

            if (found):
                newGraph.lists[i].vrtxappend(nextVrtx.vertex)

            nextVrtx = nextVrtx.next

    return newGraph


def koltsevaya_summa_List(graph1, graph2):
    newVertexes = arrOr(graph1.vertexes, graph2.vertexes)

    newSize = len(newVertexes)

    newLists = [Node() for i in range(newSize)]
    for i in range(newSize):
        newLists[i].vertex = newVertexes[i]

    newGraph = listGraph(newLists, newVertexes)

    nextVrtx, found = None, None

    forRemove = []

    for i in range(newSize):
        newVrtx1 = newGraph.vertexes[i]

        if newVrtx1 in graph1.vertexes and newVrtx1 in graph2.vertexes:
            v1 = graph1.vertexes.index(newVrtx1)
            v2 = graph2.vertexes.index(newVrtx1)

            newGraph.lists[i].next = graph1.lists[v1].next

            nextVrtx = graph2.lists[v2].next

            while (nextVrtx):
                found = findInList(newGraph.lists[i], nextVrtx.vertex)

                if (not found):
                    newGraph.lists[i].vrtxappend(nextVrtx.vertex)
                else:
                    removeVertx_List_drct(newGraph.lists[i],nextVrtx.vertex)

                nextVrtx = nextVrtx.next


        elif newVrtx1 not in graph2.vertexes:
            v1 = graph1.vertexes.index(newVrtx1)
            newGraph.lists[i].next = graph1.lists[v1].next

        else:
            v2 = graph2.vertexes.index(newVrtx1)
            newGraph.lists[i].next = graph2.lists[v2].next

        if not newGraph.lists[i].next:
            forRemove.append(i)

    # удаляем изолимрованные вершины
    for i in forRemove:
        del newGraph.lists[i]
        del newGraph.vertexes[i]

    return newGraph