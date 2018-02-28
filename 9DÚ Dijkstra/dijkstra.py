class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = float('inf')
        self.previousVertex = None
        self.edges = []


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class PriorityQueue:
    def __init__(self):
        self.head = None

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, data):
        new = self.Node(data)
        ref = self.head
        if ref is None:
            self.head = new
        elif new.data.minDistance < ref.data.minDistance:
            new.next = self.head
            self.head = new
        else:
            while (ref.next is not None) and (new.data.minDistance > ref.next.data.minDistance):
                ref = ref.next
            new.next = ref.next
            ref.next = new

    def printQueue(self):
        ref = self.head
        while ref is not None:
            print(ref.data)
            ref = ref.next

    def pop(self):
        if self.head is None:
            return None
        else:
            ret = self.head
            self.head = self.head.next
            return ret.data

    def remove(self, id):
        if id == self.head.data.id:
            self.pop()
        else:
            foo = self.head
            while foo.next.data.id != id:
                foo = foo.next
            toDelete = foo.next
            foo.next = toDelete.next


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            self.vertexes.insert(vertex.id, vertex)
        for edge in edgesToVertexes:
            self.vertexes[edge.source].edges.append(edge)

    def getVertexes(self):
        return self.vertexes

    def isInQueue(self, vertexId, queue):
        ret = False
        foo = queue.head
        while foo is not None:
            if foo.data.id == vertexId:
                ret = True
                return ret
            foo = foo.next
        return ret

    def computePath(self, sourceId):
        queue = PriorityQueue()

        for vertex in self.vertexes:
            if vertex.id == sourceId:
                vertex.minDistance = 0
            else:
                vertex.minDistance = float('inf')
            vertex.previousVertex = None
            queue.push(vertex)

        while queue.head is not None:
            vertex = queue.pop()
            for edge in vertex.edges:
                if self.isInQueue(self.vertexes[edge.target].id, queue):
                    distance = vertex.minDistance + edge.weight
                    if distance < self.vertexes[edge.target].minDistance:
                        self.vertexes[edge.target].minDistance = distance
                        self.vertexes[edge.target].previousVertex = vertex.id
                        queue.remove(edge.target)
                        queue.push(self.vertexes[edge.target])

    def getShortestPathTo(self, targetId):
        foo = targetId
        path = []
        while self.vertexes[foo].previousVertex is not None:
            path.insert(0, self.vertexes[foo])
            foo = self.vertexes[foo].previousVertex
        path.insert(0, self.vertexes[foo])
        return path

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None


#
# TEST --------------------------------------------------------------------

# vertexes = [
#     Vertex(0, "Redville"),
#     Vertex(1, "Blueville"),
#     Vertex(2, "Greenville"),
#     Vertex(3, "Orangeville"),
#     Vertex(4, "Purpleville")
# ]
#
# edges = [
#     Edge(0, 1, 5),
#     Edge(0, 2, 10),
#     Edge(0, 3, 8),
#     Edge(1, 0, 5),
#     Edge(1, 2, 3),
#     Edge(1, 4, 7),
#     Edge(2, 0, 10),
#     Edge(2, 1, 3),
#     Edge(3, 0, 8),
#     Edge(3, 4, 2),
#     Edge(4, 1, 7),
#     Edge(4, 3, 2)
# ]
#
# dijkstra = Dijkstra()
# dijkstra.createGraph(vertexes, edges)
# dijkstra.computePath(0)
# print(dijkstra.getShortestPathTo(1))
# dijkstra.computePath(1)
# print(dijkstra.vertexes[0].minDistance)
