def printListGraph(graph):
    size = len(graph)

    nextList, nextVertex, = None, None

    for i in range(size):
        nextList = graph[i]

        nextVertex = nextList

        while (nextVertex.next):
            print("|{:3d}|".format(nextVertex.vertex), end='->')
            nextVertex = nextVertex.next

        print("|{:3d}|".format(nextVertex.vertex))