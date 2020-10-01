from tools.listsGrphTools import *

class Node(object):
    def __init__(self):
        self.vertex = None
        self.next = None


def listToMatrix(matrixGraph):
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



    return graphLists