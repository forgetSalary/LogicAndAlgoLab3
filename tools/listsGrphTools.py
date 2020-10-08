def printListGraph(graph):
    size = len(graph.vertexes)

    nextList, nextVertex, = None, None

    for i in range(size):
        nextList = graph.lists[i]

        nextVertex = nextList

        while (nextVertex.next):
            print("|{:3d}|".format(nextVertex.vertex), end='->')
            nextVertex = nextVertex.next

        print("|{:3d}|".format(nextVertex.vertex))

    print("\n")