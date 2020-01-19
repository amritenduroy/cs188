class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.weights = {}
        self.visited = False

class Graph:
    def __init__(self):
        self.verteses = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.verteses[vertex.value] = vertex
            return True
        return False

    def add_path(self, from_vertex, to_vertex, weights=None):
        if to_vertex.value not in from_vertex.neighbours:
            from_vertex.neighbours.append(to_vertex.value)
            from_vertex.weights[to_vertex.value] = weights
        if from_vertex.value not in to_vertex.neighbours:
            to_vertex.neighbours.append(from_vertex.value)
            to_vertex.weights[from_vertex.value] = weights



# for k, v in graph.verteses.items():
#     print(k)
#     print(v.neighbours)
#     print(v.weights)