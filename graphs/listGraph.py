from tools.listsGrphTools import *

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

def removeVertx_List(graph, vrtx):
    v=graph.vertexes.index(vrtx)

    nextVertex, vrtxForClear, parent = None, None, None

    nextVertex = graph.lists[v].next
    while (nextVertex):
        vrtxForClear = graph.vertexes.index(nextVertex.vertex)

        parent = findFirstParent(graph.lists[vrtxForClear], vrtx)

        parent.next = parent.next.next

        nextVertex = nextVertex.next

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
        findFirstParent(dst_head, vrtxSrc).next = None

    # добавляем ребра из Src в Dst, если в последнем их нет
    while(nextVertexOfSrc.next):
        nextVertexOfSrc=nextVertexOfSrc.next

        found = findInList(dst_head,nextVertexOfSrc.vertex)
        if (not found):
            dst_head.vrtxappend(nextVertexOfSrc.vertex)

    del graph.vertexes[vrtx_index_Srs]
    del graph.lists[vrtx_index_Srs]



